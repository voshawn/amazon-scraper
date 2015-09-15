# -*- coding: utf-8 -*-
import scrapy
from amazon.items import AmazonItem


class BestsellersDeptSpider(scrapy.Spider):
    name = "bestsellersdept"
    allowed_domains = ["amazon.com"]
    start_urls = [
        'https://www.amazon.com/Best-Sellers-Appliances/zgbs/appliances/',
        'https://www.amazon.com/Best-Sellers-Arts-Crafts-Sewing/zgbs/arts-crafts/',
        'https://www.amazon.com/Best-Sellers-Automotive/zgbs/automotive/',
        'https://www.amazon.com/Best-Sellers-Baby/zgbs/baby-products/',
        'https://www.amazon.com/Best-Sellers-Cell-Phones-Accessories/zgbs/wireless/',
        'https://www.amazon.com/Best-Sellers-Computers-Accessories/zgbs/pc/',
        'https://www.amazon.com/Best-Sellers-Health-Personal-Care/zgbs/hpc/',
        'https://www.amazon.com/Best-Sellers-Home-Kitchen/zgbs/home-garden/',
        'https://www.amazon.com/Best-Sellers-Home-Improvement/zgbs/hi/',
        'https://www.amazon.com/Best-Sellers-Industrial-Scientific/zgbs/industrial/',
        'https://www.amazon.com/Best-Sellers-Kitchen-Dining/zgbs/kitchen/',
        'https://www.amazon.com/Best-Sellers-Musical-Instruments/zgbs/musical-instruments/',
        'https://www.amazon.com/Best-Sellers-Office-Products/zgbs/office-products/',
        'https://www.amazon.com/Best-Sellers-Patio-Lawn-Garden/zgbs/lawn-garden/',
        'https://www.amazon.com/Best-Sellers-Pet-Supplies/zgbs/pet-supplies/',
        'https://www.amazon.com/Best-Sellers-Sports-Outdoors/zgbs/sporting-goods/'
    ]

    # def parse(self, response):
    #     for href in response.xpath('//ul[@id="zg_browseRoot"]/ul/li/a/@href'):
    #         url = str(href.extract()).strip()
    #         # yield scrapy.Request(url, callback=self.parse_pagination)
    #         yield scrapy.Request(url, callback=self.parse_category) 

    #renamed parse to parse_category

    # def parse(self, response):
    #     for href in response.xpath(
    #         '//ul[@id="zg_browseRoot"]/ul/ul/li/a/@href'
    #     ):
    #         url = str(href.extract()).strip()
    #         print url
    #         yield scrapy.Request(url, callback=self.parse_pagination)

    #rename parse to parse_pagination

    def parse(self, response):
        for href in response.css('ol.zg_pagination a::attr(href)'):
            url = str(href.extract()).strip()
            yield scrapy.Request(url, callback=self.parse_item_link)

    def parse_item_link(self, response):
        for href in response.css('div.zg_title a::attr(href)'):
            url = str(href.extract()).strip()
            yield scrapy.Request(url, callback=self.parse_detail_page)

    def parse_detail_page(self, response):
        product = AmazonItem()
        product['name'] = response.css('h1 span.a-size-large::text').extract()
        product['url'] = response.url

        if response.xpath('//tr[@id="SalesRank"]/td[@class="value"]/text()').re_first('\d+,*\d*d*d*') == None:
            product['departmentRank'] = response.xpath('//li[@id="SalesRank"]/text()').re_first('\d+,*\d*d*d*')
        else: 
            product['departmentRank'] = response.xpath('//tr[@id="SalesRank"]/td[@class="value"]/text()').re_first('\d+,*\d*d*d*')

        try:
            product['department'] = str(response.xpath(
                '''//div[@id="wayfinding-breadcrumbs_feature_div"]
                /ul/li/span/a/text()''').extract()[0]).strip()
        except IndexError:
            pass

        try:
            product['subDepartment'] = str(response.xpath(
                '''//div[@id="wayfinding-breadcrumbs_feature_div"]
                /ul/li/span/a/text()''').extract()[1]).strip()
        except IndexError:
            pass
        try:
            product['price'] = response.css(
                'td span.a-color-price::text').re('^[$]\d+\.\d+')[0]
        except IndexError:
            pass
        try:
            product['reviews'] = response.css(
                '''div.feature div.a-spacing-none span.a-declarative
                 span.a-size-base::text''').re('\d+,*\d*d*d*')[0]
        except IndexError:
            pass

        
        if response.xpath('//tr/td[@class="bucket"]/div[@class="content"]/ul/li[contains(.,"Shipping Weight")]').re('\d.*pounds|ounces') == []:
            try:
                product['weight'] = response.css(
                    'tr.size-weight td.value::text').extract()[0]
            except IndexError:
                pass
        else:
            product['weight'] = response.xpath('//tr/td[@class="bucket"]/div[@class="content"]/ul/li[contains(.,"Shipping Weight")]').re('\d.*pounds|\d.*ounces')

        if response.xpath('//tr/td[@class="bucket"]/div[@class="content"]/ul/li[contains(.,"Dimensions")]').re('\d.*inches') == []:
            try:
                product['dimensions'] = response.css(
                    'tr.size-weight td.value::text').extract()[1]
            except IndexError:
                pass
        else:
            product['dimensions'] = response.xpath('//tr/td[@class="bucket"]/div[@class="content"]/ul/li[contains(.,"Dimensions")]').re('\d.*inches')

        yield product
