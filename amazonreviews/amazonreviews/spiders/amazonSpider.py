# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonreviewsItem

class AmazonspiderSpider(scrapy.Spider):
    name = 'spiderman'
    start_urls = ['https://www.amazon.in/s?k=mobiles&ref=nb_sb_noss_2']

    def parse(self, response):
        item = AmazonspiderSpider()
        name = response.css('.a-size-medium::text').extract() #single class uses text inside
        price = response.css('.a-spacing-top-mini:nth-child(1) .a-color-price , .a-spacing-top-small .a-price:nth-child(1) .a-price-whole').css('::text').extract()
        item['productName'] = name
        item['productPrice'] = price

        yield item

