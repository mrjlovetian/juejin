# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JuejinItem(scrapy.Item):
    buildTime = scrapy.Field()
    updatedAt = scrapy.Field()
    originalUrl = scrapy.Field()
    screenshot = scrapy.Field()
    content = scrapy.Field()
    title = scrapy.Field()
    viewsCount = scrapy.Field()
    summaryInfo = scrapy.Field()


