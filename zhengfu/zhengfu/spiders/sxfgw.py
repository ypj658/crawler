# -*- coding: utf-8 -*-
import scrapy
from items import ZhengfuItem


class sxSpider(scrapy.Spider):
    name = "sxfgw"
    start_urls = ['http://www.sndrc.gov.cn/newstyle/pub_newschannel.asp?chid=100073']
    baseUrl = 'http://www.sndrc.gov.cn'

    # 只抓取通知页面第一页
    def parse(self, response):
        print("start crawl")
        for li in response.xpath("//div[@id='lmrwkzw']//li"):
            title = "".join(li.xpath("./a/text()").extract())
            url = self.baseUrl + "".join(li.xpath("./a/@href").extract())
            date = "".join(li.xpath("./span/text()").extract())
            # print("%.10s\t%s\t%s" %(title,url,date))
            item = ZhengfuItem()

            item['title'] = title
            item['href'] = url
            item['source'] = '陕西省发改委'
            item['publish_date'] = date
            item['content'] = ''
            item['publisher'] = ''
            yield item
