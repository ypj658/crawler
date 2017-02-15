# -*- coding: utf-8 -*-
from datetime import datetime

import scrapy
from scrapy import Request
from scrapy.utils.project import get_project_settings

from items import ZhengfuItem


class sxgxtSpider(scrapy.Spider):
    name = "sxgxt"
    # allowed_domains = ["sxgxt.gov.cn"]
    start_urls = ["http://www.sxgxt.gov.cn/ggzdt/index.jhtml"]
    baseUrl = "http://www.sxgxt.gov.cn"

    # 只抓取通知页面第一页
    def parse(self, response):
        print("start crawl")
        for li in response.xpath("//div[@class='list1-new']//li"):
            title = "".join(li.xpath("./a/text()").extract())
            url = "".join(li.xpath(".//a/@href").extract())
            d = "".join(li.xpath("./span/text()").extract())[1:-1]  # [07-16]
            # date = str(datetime.now().year) + "-" + d
            date =d

            # print("%.10s\t%s\t%s" %(title,url,date))

            item = ZhengfuItem()

            item['title'] = title
            item['href'] = url
            item['source'] = '陕西省工信厅'
            item['publish_date'] = date
            item['content'] = ''
            item['publisher'] = ''
            yield item

            # def __init__(self, **kwargs):
            #     super().__init__(**kwargs)
            #     settings = get_project_settings()
            #     self.KeyWords = settings.get("KEY_WORDS")
            #     self.max_days = settings.get("MAX_BEFOR_DAYS")
            #     self.log(self.KeyWords)
            #
            # def __del__(self):
            #     # print("gxbSpider类结束\n")
            #     pass
            #
            # # only crawl the first page
            # def parse(self, response):
            #
            #     items = response.xpath("//div[@class='list1-new']//li")
            #     for item in items:
            #         isSubject = False
            #         # 判断抓取的链接标题中是否含有目标关键字
            #         url_title = "".join(item.xpath("./a/text()").extract())
            #         for key in self.KeyWords:
            #             if key in url_title:
            #                 isSubject = True
            #                 self.log(url_title)
            #                 break
            #
            #         if isSubject:
            #             d = "".join(item.xpath("./span/text()").extract())[1:-1]  # [07-16]
            #             publish_date = str(datetime.now().year) + "-" + d
            #             publish_date = datetime.strptime(publish_date, "%Y-%m-%d")
            #             days = (datetime.now() - publish_date).days
            #             if days <= self.max_days:
            #                 content_url = "".join(item.xpath(".//a/@href").extract())
            #                 yield Request(content_url, callback=self.parse_content)
            #
            # def parse_content(self, response):
            #     item = ZhengfuItem()
            #     item["title"] = "".join(response.xpath(
            #         "//h1[@id='con_title']/text()").extract())
            #
            #     try:
            #         date = "".join(response.xpath("//span[@id='con_time']/text()").extract())  # 日期：2016年12月22日      来源：科技部
            #         date = date.split("：")[1]
            #         item["publish_date"] = date.replace("年", "-").replace("月", "-").replace("日", "")  # 发布时间：2016-09-14
            #     except Exception as e:
            #         self.log(e)
            #         item["publish_date"] = ""
            #
            #     item["publisher"] = "陕西省工信厅"
            #
            #     item["source"] = "陕西省工信厅"
            #     item["href"] = response.url
            #     item["content"] = "".join(response.xpath("//div[@class='content']").extract())
            #
            #     yield item
