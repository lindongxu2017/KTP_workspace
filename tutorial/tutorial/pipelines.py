# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from pymysql.converters import escape_string

class TutorialPipeline:
    def process_item(self, item, spider):
        return item

class yingcaiPipeline:
    def process_item(self, item, spider):
        trim_item = {}
        for i in item.keys():
            trim_item[i] = str(item[i]).replace('\n', '').replace(' ', '').replace('\\n', '')
        return trim_item

class mysqlPipeline:
    def open_spider(self, spider):
        # self.conn = pymysql.connect(host='localhost',user='root',passwd='123456',db='scrapy-app')  #连接数据库
        self.conn = pymysql.connect(host='localhost',user='root',passwd='123456',db='yingcai')  #连接数据库
    def process_item(self, item, spider):
        #添加数据到表中
        obj = {}
        for key in item:
            obj[key] = escape_string(item[key])
        sql = ''
        if item:
            if item['dbname'] == 'book_list':
                sql = "INSERT INTO book_list (`title`,`link`,`desc`,`price`,`panelimg`,`bookfaceimg`) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (obj['title'],obj['link'],obj['desc'],obj['price'],obj['panelimg'],obj['bookfaceimg'])
            if item['dbname'] == 'book_detail':
                sql = "INSERT INTO book_detail (`sample`,`link`,`bookname`,`dt`,`dd`) VALUES ('%s', '%s', '%s', '%s', '%s')" % (obj['sample'],obj['link'],obj['bookname'],obj['dt'],obj['dd'])
            if item['dbname'] == 'job_list':
                sql = "INSERT INTO job_list (`title`,`enterprise`,`salary`,`address`,`number`,`term`,`update`,`fulicontent`,`detail`,`contact`) VALUES ('%s', '%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s')" % (obj['title'],obj['enterprise'],obj['salary'],obj['address'],obj['number'],obj['term'],obj['update'],obj['fulicontent'],obj['detail'],obj['contact'])
            try:
                self.conn.query(sql)
                self.conn.commit()#执行添加
            except:
                pass
    def close_spider(self, spider):
        self.conn.close()  #关闭连接
        yield item
