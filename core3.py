#from spiders.symbolCrawl import SymbolcrawlSpider
from spiders.historydata3 import Historydata3Spider

# scrapy api
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner,CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

configure_logging()
settings = get_project_settings()
runner = CrawlerRunner(settings)

@defer.inlineCallbacks
def crawl():
    #yield runner.crawl(SymbolcrawlSpider)
    yield runner.crawl(Historydata3Spider)

crawl()
reactor.run()