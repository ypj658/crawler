# -*- coding: utf-8 -*-
from datetime import datetime

import scrapy
from scrapy import Request
from scrapy.utils.project import get_project_settings

from items import ZhengfuItem


class KjbSpider(scrapy.Spider):
    name = "kjb"
    # allowed_domains = ["most.gov.cn"]
    start_urls = ["http://www.most.gov.cn/tztg/index.htm"]
    baseUrl = "http://www.most.gov.cn/tztg"

    # 只抓取通知页面第一页
    def parse(self, response):
        print("start crawl")
        for li in response.xpath("//td[@class='STYLE30']"):
            title = "".join(li.xpath("./a/text()").extract()).strip()
            url = self.baseUrl + "".join(li.xpath("./a/@href").extract())[1:]

            c = li.extract()
            d = c[c.find("</a>") + 4:]
            date = d[d.find("(") + 1:d.find(")")]

            # print("%.10s\t%s\t%s" %(title,url,date))

            item = ZhengfuItem()

            item['title'] = title
            item['href'] = url
            item['source'] = '科技部'
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
            # def parse(self, response):
            #
            #     items = response.xpath("//td[@class='STYLE30']")
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
            #             c = item.extract()
            #             d = c[c.find("</a>") + 4:]
            #             publish_date = d[d.find("(") + 1:d.find(")")]
            #             # publish_date = "".join(li.xpath("./span/a/text()").extract())
            #             publish_date = datetime.strptime(publish_date, "%Y-%m-%d")
            #             days = (datetime.now() - publish_date).days
            #             if days <= self.max_days:
            #                 content_url = self.baseUrl + "".join(item.xpath("./a/@href").extract())[1:]
            #                 yield Request(content_url, callback=self.parse_content)
            #
            # def parse_content(self, response):
            #     item = ZhengfuItem()
            #     item["title"] = "".join(response.xpath(
            #         "//div[@id='Title']/text()").extract()).replace(" ", "")
            #
            #     try:
            #         info = "".join(response.xpath("//div[@class='gray12 lh22']/text()").extract())  # 日期：2016年12月22日      来源：科技部
            #         # ds=[d for d in info.split(r"\n")]
            #         info = info.replace("\xa0", "").replace("\n", "")
            #         date = info.split("：")[1]
            #
            #         item["publish_date"] = date.replace("年", "-").replace("月", "-").replace("日", "")  # 发布时间：2016-09-14
            #         # item["publisher"] = ds[1].split("：")[1]  # 来源：中小企业局
            #     except Exception as e:
            #         self.log(e)
            #         item["publish_date"] = ""
            #
            #     item["publisher"] = "科技部"
            #
            #     item["source"] = "科技部"
            #     item["href"] = response.url
            #     item["content"] = "".join(response.xpath("//div[@id='Zoom']").extract())
            #
            #     yield item
