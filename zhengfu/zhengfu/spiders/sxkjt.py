# -*- coding: utf-8 -*-
import scrapy
from items import ZhengfuItem


class sxkjtSpider(scrapy.Spider):
    name = "sxkjt"
    start_urls = [
        'http://www.sninfo.gov.cn:8083/initSnTwoPageArticleTypeList.do?method=initSnTwoPageArticleTypeList&articleTypeId=20549']
    baseUrl = 'http://www.sninfo.gov.cn:8083/'

    # 只抓取通知页面第一页
    def parse(self, response):
        print("start crawl")
        for li in response.xpath("//table[@id='table1']//tr")[:-1]:
            title = "".join(li.xpath("./td[1]/a/text()").extract()).strip()
            url = self.baseUrl + "".join(li.xpath("./td[1]/a/@href").extract())[1:]
            date = "".join(li.xpath("./td[3]/a/text()").extract()).strip()
            # print("%.10s\t%s\t%s" %(title,url,date))

            item = ZhengfuItem()

            item['title'] = title
            item['href'] = url
            item['source'] = '陕西省科技厅'
            item['publish_date'] = date
            item['content'] = ''
            item['publisher'] = ''

            yield item
