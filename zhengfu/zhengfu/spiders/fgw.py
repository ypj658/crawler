# -*- coding: utf-8 -*-
import scrapy


class FgwSpider(scrapy.Spider):
    name = "fgw"
    allowed_domains = ["sdpc.gov.cn"]
    start_urls = ['http://sdpc.gov.cn/']

    def parse(self, response):
        pass
