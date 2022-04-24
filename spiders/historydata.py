import scrapy
from pipelines import LoadSymbol
import numpy as np
from crawldata import CrawlDataSymbol

class HistorydataSpider(scrapy.Spider):
    name = 'historydata'
    allowed_domains = ['s.cafef.vn']
    run = LoadSymbol.connectDB()
    urlhistorys = []
   
    for id, symbol, urlsymbol in run:
        urlhistorys.append(urlsymbol)

    start_urls = urlhistorys

    def parse(self, response):
        url = response.url
        symbol = response.xpath('//*[@id="symbolbox"]/text()').get().split()[0]
        filename = 'HistorydataSpider.csv'
        CrawlDataSymbol(symbol, url, filename)
