import scrapy
from pipelines import LoadSymbol
import numpy as np
from crawldata import CrawlDataSymbol

class Historydata1Spider(scrapy.Spider):
    name = 'historydata1'
    allowed_domains = ['s.cafef.vn']
    run = LoadSymbol.connectDB()
    urlhistorys = []
   
    for i in range(300,587):
        urlhistorys.append(run[i][2])

    start_urls = urlhistorys
    print(start_urls)
    def parse(self, response):
        url = response.url
        symbol = response.xpath('//*[@id="symbolbox"]/text()').get().split()[0]
        filename = 'Historydata1Spider.csv'
        CrawlDataSymbol(symbol, url, filename)
