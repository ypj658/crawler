# -*- coding: utf-8 -*-
import scrapy
from items import ZhengfuItem


class fgwSpider(scrapy.Spider):
    name = "fgw"
    start_urls = ['http://www.sdpc.gov.cn/zcfb/zcfbtz/index.html']
    baseUrl = 'http://www.sdpc.gov.cn/zcfb/zcfbtz/'

    # 只抓取通知页面第一页
    def parse(self, response):
        print("start crawl")
        for li in response.xpath("//li[@class='li']"):
            title = "".join(li.xpath("./a/text()").extract())
            url = self.baseUrl + "".join(li.xpath("./a/@href").extract())[5:]
            date = "".join(li.xpath("./font[@class='date']/text()").extract()).replace("/", "-")
            # print("%.10s\t%s\t%s" %(title,url,date))
            item = ZhengfuItem()

            item['title'] = title
            item['href'] = url
            item['source'] = '发改委'
            item['publish_date'] = date
            item['content'] = ''
            item['publisher'] = ''
            yield item
