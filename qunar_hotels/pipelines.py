# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import datetime
import os
import pymongo


class QunarHotelsPipeline(object):
    def open_spider(self, spider):
        today = datetime.datetime.now().strftime('%Y%m%d')
        self.path = r'json/%s' % today
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        self.client = pymongo.MongoClient()
        self.db = self.client.qunr
        self.collection = self.db[today]

    def close_spider(self, spider):
        self.db.close()
        self.client.close()
        

    def process_item(self, item, spider):

        self.write_in_json(item)

        return item

    def write_in_mongo(self, hotel_info):


        self.collection.insert(hotel_info)


    def write_in_json(self,item):
        city_url = item['city_url'][0]
        with open(os.path.join(self.path, city_url) + '.json', 'w', encoding='utf-8') as fp:
            fp.write('{')
            for hotel in item['result']:
                hotel_info = {
                    "city":city_url,
                    "dname": hotel[0],
                    "qname": hotel[1],
                    "group": hotel[2],
                    "groupType": hotel[3],
                    "hotDegree": hotel[4]
                }
                fp.write(json.dumps(hotel_info, ensure_ascii=False) + ',\n')
                self.write_in_mongo(hotel_info)
            fp.write('}')
