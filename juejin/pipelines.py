# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class JuejinPipeline(object):
    def process_item(self, item, spider):
        db = pymysql.connect('localhost', 'root', '897011805', 'yhj')
        cursor = db.cursor()
        sql = '''INSERT INTO juejin VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')'''%(item['buildTime'], item['updatedAt'], item['originalUrl'], item['screenshot'], item['content'], item['title'], item['viewsCount'], item['summaryInfo'])
        cursor.execute(sql)
        cursor.commit()
        db.close()
        return item