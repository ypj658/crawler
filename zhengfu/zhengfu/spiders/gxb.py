# -*- coding: utf-8 -*-
from datetime import datetime
import sys

import scrapy
from scrapy import Request
from scrapy.utils.project import get_project_settings

from items import ZhengfuItem


class GxbSpider(scrapy.Spider):
    name = "gxb"
    allowed_domains = ["miit.gov.cn"]
    start_urls = ["http://www.miit.gov.cn/n1146290/n4388791/index.html"]
    baseUrl = "http://www.miit.gov.cn"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        settings = get_project_settings()
        self.KeyWords = settings.get("KEY_WORDS")
        self.max_days = settings.get("MAX_BEFOR_DAYS")
        self.log(self.KeyWords)

    def __del__(self):
        # print("gxbSpider类结束\n")
        pass

    def parse(self, response):
        for li in response.xpath("//div[@class='clist_con']//li"):
            isSubject = False
            # 判断抓取的链接标题中是否含有目标关键字
            url_title = "".join(li.xpath("./a/text()").extract())
            for key in self.KeyWords:
                if key in url_title:
                    isSubject = True
                    self.log(url_title)
                    break

            if isSubject:
                publish_date = "".join(li.xpath("./span/a/text()").extract())
                publish_date = datetime.strptime(publish_date, "%Y-%m-%d")
                days = (datetime.now() - publish_date).days
                if days <= self.max_days:
                    content_url = self.baseUrl + "".join(li.xpath("./a/@href").extract())[5:]
                    yield Request(content_url, callback=self.parse_content)

    def parse_content(self, response):
        item = ZhengfuItem()
        item["title"] = "".join(response.xpath(
            "//h1[@id='con_title']/text()").extract()).replace(" ", "")

        try:
            info = response.xpath("//div[@class='cinfo center']//span/text()")
            item["publish_date"] = info[0].extract().split("：")[1]  # 发布时间：2016-09-14
            item["publisher"] = info[1].extract().split("：")[1]  # 来源：中小企业局
        except Exception as e:
            self.log(e)
            item["publisher"] = ""

        item["source"] = "工信部"
        item["href"] = response.url
        item["content"] = "".join(response.xpath("//div[contains(@class,'content')]").extract())

        yield item
