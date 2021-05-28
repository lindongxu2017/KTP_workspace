import scrapy
import os
import sys
import logging
import datetime
import re
import json
import requests
import time

from io import BytesIO
import urllib.request
from PIL import Image
import base64

from tutorial.items import yingcaiItem

# 个人账号
# APIKEY = 'W0oX0qwUQwAwX7F0wtf0ShcH'
# SECRETKEY = 'i6AQVoPmCqxuYPCrlnyr6KXZipRxSP5f'


# 公司账号
APIKEY = 'Hq9WBvFuMAq6s0G5ogG06Eui'
SECRETKEY = 'wYvUG9CVGz8tGOzYXmW3CcqzBVhKGOyp'
HOST = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + APIKEY + '&client_secret=' + SECRETKEY
TOKEN_RESPONSE = requests.get(HOST)
if TOKEN_RESPONSE:
    ACCESS_TOKEN = TOKEN_RESPONSE.json()['access_token']

to_day = datetime.datetime.now()
file_name = 'scrapy_{}_{}_{}.log'.format(to_day.year, to_day.month, to_day.day)
_path1 = os.path.abspath(__file__)
_path2 = os.path.dirname(_path1)
_path3 = os.path.dirname(_path2)
_path4 = os.path.dirname(_path3)

def myTrim(_str):
    return _str.replace(' ', '').replace('\n', '')

def get_img_base64_from_url(url, max_length=800):
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        ls_f = base64.b64encode(BytesIO(response.content).read())
        return ls_f
    except:
        return ''

def ImageOcrToNumber(src):
    img_base64 = get_img_base64_from_url(src)
    params = {"image": img_base64}
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/numbers" + "?access_token=" + ACCESS_TOKEN
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())
        try:
            _number = response.json()['words_result'][0]['words']
        except:
            _number = ''
        return _number

class yingcaiSpider(scrapy.Spider):
    name = 'yingcai'
    # allowed_domains = ['qushigong.com']
    cur_page = 1
    base_url = 'https://b-worker.buildhr.com/so/p'
    domain = 'https://b-worker.buildhr.com/'
    cur_start = base_url + str(cur_page) + '.html'
    start_urls = [
        cur_start
    ]

    def parse(self, response):
        info_list = response.css('.item-job')
        if info_list:
            for el in info_list:
                url = el.css('.job-status a::attr(href)').extract()[0]
                logging.warning(url)
            if self.cur_page < 100:
                self.cur_page = self.cur_page + 1
                next_link = self.base_url + str(self.cur_page) + '.html'
                yield scrapy.Request(next_link, callback=self.parse)                
        else:
            if self.cur_page < 100:
                self.cur_page = self.cur_page + 1
                next_link = self.base_url + str(self.cur_page) + '.html'
                yield scrapy.Request(next_link, callback=self.parse)
            pass
        if self.cur_page == 100:
            _file = open(_path4 + "\/log\/" + file_name, "r")
            for line in _file.readlines():
                try:
                    detail_url = self.domain + line.split('WARNING: ')[1]
                    yield scrapy.Request(detail_url, callback=self.detailHandler)
                except:
                    pass
            _file.close()

    def detailHandler(self, response):
        # url = response.url
        export_item = yingcaiItem()
        export_item['dbname'] = 'job_list'
        # 电话号码处理
        phone = response.css('.contact-us > div p *::text').extract()
        trim_str = '\n'.join(phone).replace(' ', '')
        if re.search('电话', trim_str):
            phone_list = trim_str.split('电话：')[1].split(',')
            imgs = response.css('.contact-us > div p img::attr(src)').extract()
            item_phone_text = []
            for index in range(len(phone_list)):
                phone_item = phone_list[index]
                if index == 0:
                    phone_item = phone_list[index][1:]
                for order in range(len(imgs)):
                    img = imgs[order]
                    img_src = 'https://' + img.split('//')[1]
                    sys.stdout.flush() # 刷新缓冲区
                    time.sleep(0.5)
                    img_number = ImageOcrToNumber(img_src) # 人工智能识别图片文字
                    if index == order:
                        real_number = phone_item.replace('\n', img_number)
                        item_phone_text.append(real_number)
            export_item['contact'] = item_phone_text
            export_item['title'] = response.css('.job-name::text').extract()[0]
            export_item['enterprise'] = response.css('.enterprise-name a::text').extract()[0]
            export_item['salary'] = response.css('.job-salary::text').extract()[0]

            address_dall = response.xpath('//p[@class="job-address"]')
            export_item['address'] = address_dall.xpath('string(.)').extract()[0].replace('工作地点：', '')

            i_dall = response.css('.other-info p')
            for i in range(len(i_dall)):
                if i == 0:
                    export_item['number'] = i_dall[i].xpath('string(.)').extract()[0].replace('招聘人数：', '')
                if i == 1:
                    export_item['term'] = i_dall[i].xpath('string(.)').extract()[0].replace('招聘期：', '')
                if i == 2:
                    export_item['update'] = i_dall[i].xpath('string(.)').extract()[0].replace('更新日期：', '')

            export_item['fulicontent'] = response.css('.fuli-i::text').extract()
            export_item['detail'] = response.css('.detail-other .value *::text').extract()
            yield export_item
        else:
            yield {}
        
        