# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class ZhengfuItem(scrapy.Item):
    """
    用于存储从政府网站爬来的数据
    """
    title = Field()
    href = Field()
    content = Field()
    source = Field()
    publisher = Field()
    publish_date = Field()
    catch_date = Field()
