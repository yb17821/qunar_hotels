# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class QunarHotelsPipeline(object):
    # def open_spider(self,spider):
    #     self.f = open('hotel.json','w',encoding='utf-8')
    # def close_spider(self, spider):
    #     self.f.close()
    def process_item(self, item, spider):
        city_url = item['city_url'][0]
        with open(r'json/%s.json' % city_url,'w',encoding='utf-8') as fp:
            fp.write('{')
            for hotel in item['result']:
                hotel_info = {
                    "dname": hotel[0],
                    "qname": hotel[1],
                    "group": hotel[2],
                    "groupType": hotel[3],
                    "hotDegree": hotel[4]
                }
                fp.write(json.dumps(hotel_info,ensure_ascii=False)+',\n')
            fp.write('}')
        return item
