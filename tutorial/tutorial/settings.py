# Scrapy settings for tutorial project
#
import datetime
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'

# 连接数据库

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'
# 模拟浏览器访问
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 降低请求速率
# CONCURRENT_REQUESTS = 16

# JSON文件导出Unicode字符转换中文
from scrapy.exporters import JsonLinesItemExporter

class CustomJsonLinesItemExporter(JsonLinesItemExporter):
  def __init__(self, file, **kwargs):
    super (CustomJsonLinesItemExporter, self).__init__(file, ensure_ascii=False, **kwargs)

#启用新定义的Exporter类\
FEED_EXPORTERS = {
  'json':'tutorial.settings.CustomJsonLinesItemExporter',
}

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 降低下载速率
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False
# 日志
LOG_ENABLED = True
to_day = datetime.datetime.now()
log_file_path = 'log/scrapy_{}_{}_{}.log'.format(to_day.year, to_day.month, to_day.day)
LOG_LEVEL = 'WARNING'
LOG_FILE = log_file_path
LOG_ENABLED = True

# 失败禁止重新链接
RETRY_ENABLED = False

# 有些站点(基于2013年的经验数据，之多有1%)声明其为 ajax crawlable 。 这意味着该网站提供了原本只有ajax获取到的数据的纯HTML版本。 网站通过两种方法声明:
# 在url中使用 #! - 这是默认的方式;
# 使用特殊的meta标签 - 这在”main”, “index” 页面中使用。
AJAXCRAWL_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tutorial.middlewares.TutorialSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'tutorial.middlewares.TutorialDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'tutorial.pipelines.TutorialPipeline': 300,
   'tutorial.pipelines.yingcaiPipeline': 400,
  #  'tutorial.pipelines.mysqlPipeline': 500
}
# 下载图片存储路径
# IMAGES_STORE = r'C:\Users\-\Desktop\scrapy'
# 缩略图生成
# IMAGES_THUMBS = {
#   'small': (50, 50),
#   'big': (270, 270),
# }
# 高度限制
# IMAGES_MIN_HEIGHT
# 宽度限制
# IMAGES_MIN_WIDTH
# 允许的状态码
HTTPERROR_ALLOWED_CODES = [301]

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
