# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    reviews = scrapy.Field()
    weight = scrapy.Field()
    dimensions = scrapy.Field()
    url = scrapy.Field()
    department = scrapy.Field()
    subDepartment = scrapy.Field()
    departmentRank = scrapy.Field()
    pass
