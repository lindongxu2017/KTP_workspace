# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    dbname = scrapy.Field() # 存储表名
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    price = scrapy.Field()
    panelimg = scrapy.Field()
    bookfaceimg = scrapy.Field()

class ImageItem(scrapy.Item):
    dbname = scrapy.Field() # 存储表名
    sample = scrapy.Field()
    link = scrapy.Field()
    bookname = scrapy.Field()
    dt = scrapy.Field()
    dd = scrapy.Field()

class laowuItem(scrapy.Item):
    link = scrapy.Field()

class yingcaiItem(scrapy.Item):
    dbname = scrapy.Field() # 存储表名
    # id = scrapy.Field() # id
    title = scrapy.Field() # 项目名称
    enterprise = scrapy.Field() # 企业名称
    salary = scrapy.Field() # 薪酬
    address = scrapy.Field() # 工作地点
    number = scrapy.Field() # 招聘人数
    term = scrapy.Field() # 招聘期限
    update = scrapy.Field() # 更新日期
    fulicontent = scrapy.Field() # 福利待遇
    # skill = scrapy.Field() # 职业要求
    detail = scrapy.Field() # 职位描述
    contact = scrapy.Field() # 联系方式