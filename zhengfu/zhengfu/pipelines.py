# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from dbhelpler.dbHelper import dbHelper


class SaveToSqlite(object):
    def __init__(self):
        self.db = dbHelper()

    def process_item(self, item, spider):
        self.db.save(item)
