import scrapy
import os
import logging
import datetime
import re
import json
import requests

from tutorial.items import laowuItem

to_day = datetime.datetime.now()
file_name = 'scrapy_{}_{}_{}.log'.format(to_day.year, to_day.month, to_day.day)

class LaowuSpider(scrapy.Spider):
    name = 'laowu'
    # allowed_domains = ['qushigong.com']
    cur_page = 1
    base_url = 'https://www.qushigong.com/zhaogong/?page='
    cur_start = base_url + str(cur_page)
    start_urls = [
        cur_start
    ]
    def parse(self, response):

        _path1 = os.path.abspath(__file__)
        _path2 = os.path.dirname(_path1)
        _path3 = os.path.dirname(_path2)
        _path4 = os.path.dirname(_path3)
        _file = open(_path4 + "\/log\/" + file_name, "r")

        for line in _file.readlines():
            try:
                detail_url = line.split('WARNING: ')[1]
                yield scrapy.Request(detail_url, callback=self.detailHandler)
            except:
                pass
            
        _file.close()

        # info_list = response.css('.inc.cmsHdmC ul li')
        # if info_list:
        #     for el in info_list:
        #         url = el.css('a::attr(href)').extract()[0]
        #         logging.warning(url)
        #     if self.cur_page < 2:
        #         self.cur_page = self.cur_page + 1
        #         next_link = self.base_url + str(self.cur_page)
        #         yield scrapy.Request(next_link, callback=self.parse)
        #     else:
                # _path1 = os.path.abspath(__file__)
                # _path2 = os.path.dirname(_path1)
                # _path3 = os.path.dirname(_path2)
                # _path4 = os.path.dirname(_path3)
                # _file = open(_path4 + "\/log\/" + file_name, "r")
                # for line in _file.readlines():
                #     try:
                #         detail_url = line.split('WARNING: ')[1]
                #         yield scrapy.Request(detail_url, callback=self.detailHandler)
                #     except:
                #         pass
                    
                # _file.close()
        # else:
        #     pass
    def detailHandler(self, response):
        item = laowuItem()
        url = response.url
        _id = re.findall("\d+", url)[0]
        # print(_id)
        get_phone_baseurl = 'http://m.qushigong.com/job/get_phone?id=' + _id
        headers = {
            'Host': 'm.qushigong.com',
            'Connection': 'keep-alive',
            'Content-Length': '0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Origin': 'http://m.qushigong.com',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1326.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63010200)',
            'Referer': 'http://m.qushigong.com/zhaogong/sc/z' + str(_id) + '.html',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4',
            'Cookie': 'SE001=c33osoeis9dmie5k45b4sm9qa986iqtv; qsgscanLogs424408=%7B%22base_time%22%3A1621473451%2C%22rows%22%3A%7B%22_1428170%22%3A7818%2C%22_1427117%22%3A7811%2C%22_1428040%22%3A5622%2C%22_1428008%22%3A4887%2C%22_1427998%22%3A4881%2C%22_1427997%22%3A4717%2C%22_1427683%22%3A137%2C%22_1427679%22%3A65%7D%7D; Hm_lvt_4ad499e0d58ccae94153b02ef16fe356=1621473453; Hm_lpvt_4ad499e0d58ccae94153b02ef16fe356=1621481275'
        }
        params = {"id": _id}
        # print(params)

        result = requests.post(get_phone_baseurl, headers=headers, data=params)
        print(result)

        
