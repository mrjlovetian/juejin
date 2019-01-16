# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from juejin.items import JuejinItem


class JjSpider(CrawlSpider):
    name = 'jj'
    allowed_domains = ['juejin']
    start_urls = ['https://timeline-merger-ms.juejin.im/v1/get_entry_by_rank?src=web&before=11.309336047596&limit=200&category=all']

    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )

    def parse(self, response):
        datas = response.body['d']['entrylist']
        for va in datas:
            print('aaaaaaaaaaaaaaaaaaaaaaaaaaaa%s'%(va['title']))
            item = JuejinItem()
            item['buildTime'] = va['buildTime']
            item['updatedAt'] = va['updatedAt']
            item['originalUrl'] = va['originalUrl']
            item['screenshot'] = va['screenshot']
            item['content'] = va['content']
            item['title'] = va['title']
            item['viewsCount'] = va['viewsCount']
            item['summaryInfo'] = va['summaryInfo']
            yield item
        
        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
