# -*- coding: utf-8 -*-
import scrapy


class ScrapyTestSpider(scrapy.Spider):
    name = 'scrapy_test'
    allowed_domains = ['coi.hzau.edu.cn']
    start_urls = ['http://coi.hzau.edu.cn/']

    def parse(self,response):
        div=response.xpath("//li[@class]").extract()
        for i in div:
            print(i)
