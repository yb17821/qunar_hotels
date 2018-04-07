# -*- coding: utf-8 -*-
import scrapy
import re
from .qne import Qnr
from scrapy import Request


class CitysSpider(scrapy.Spider):
    name = 'citys'
    allowed_domains = ['hotel.qunar.com']

    def start_requests(self):
        qnr = Qnr()
        urls = qnr.get_url()
        for url in urls:
            yield Request(url, callback=self.parse)

    def parse(self, response):

        result = re.compile(
            '{"dname":"(\w+?)","qname":"(\w+?)","group":"(\w+?)","groupType":"(\w+?)","hotDegree":(\d+?)}').findall(
            response.text)
        city_url = re.compile('"cityUrl":"(\w+?)"').findall(response.text)
        yield {'city_url':city_url,'result':result}
