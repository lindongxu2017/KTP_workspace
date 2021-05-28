import scrapy
import sys
import time
from tutorial.items import TutorialItem
from tutorial.items import ImageItem

class doubanSpider(scrapy.Spider):
    name = "douban"
    # allowed_domains = ["market.douban.com"]
    cur_page = 1
    page_num = '18'
    base_url = "https://market.douban.com/book/?utm_campaign=book_freyr_section&utm_source=douban&utm_medium=pc_web&page="
    cur_start = base_url + str(cur_page) + "&page_num=" + page_num + "&"
    start_urls = [ cur_start ]

    all_books = []

    def parse(self, response):
      book_list = response.css('.book-item')
      item = TutorialItem()
      print('---------- start page %s ----------' % self.cur_page)
      for el in book_list:
        item['dbname'] = 'book_list'
        item['title'] = el.css('.book-brief h3::text').extract()[0]
        item['link'] = el.css('a::attr(href)').extract()[0]
        item['desc'] = el.css('.book-quote > p::text').extract()[0]
        item['price'] = '￥' + el.css('.book-price > i::text').extract()[0]
        item['panelimg'] = el.css('.panel-img img::attr(src)').extract()[0]
        item['bookfaceimg'] = el.css('.bookface-img img::attr(src)').extract()[0]
        detail_url_str = el.css('.book-item a::attr(href)').extract()[0]
        self.all_books.append(detail_url_str)
        sys.stdout.flush() # 刷新缓冲区
        time.sleep(0.3)
        print('scrapying', item['link'])
        yield item

      if book_list:
        self.cur_page = self.cur_page + 1
        next_link = self.base_url + str(self.cur_page) + "&page_num=" + self.page_num + "&"
        yield scrapy.Request(next_link, callback=self.parse)
      else:
        # 开始爬取详情页
        print('书籍数量：')
        print(len(self.all_books))
        # self.all_books.reverse()
        # for url in self.all_books:
        #   yield scrapy.Request(url, callback = self.detail)

    def detail(self, response):
      dt = response.css('.text-right dl dt::text').extract()
      dd = response.css('.text-right dl dd em::text').extract()
      item = ImageItem()
      item['dbname'] = 'book_detail'
      item['link'] = response.url
      try:
        item['sample'] = response.css('.img-left img::attr(src)').extract()[0]
      except:
        item['sample'] = ''
      item['bookname'] = response.css('.book-breintro > h3::text').extract()[0]
      item['dt'] = ','.join(dt)
      if dd and dd[0]:
        del(dd[0])
      item['dd'] = ','.join(dd)
      yield item