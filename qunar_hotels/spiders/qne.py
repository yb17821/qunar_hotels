import requests
import re
import time


class Qnr():
    def __init__(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
        city_name_url = 'http://hotel.qunar.com/render/hoteldiv.jsp?&__jscallback=XQScript_8'
        session = requests.Session()
        response = session.get(city_name_url, headers = headers)
        response.encoding = 'utf-8'
        self.hot_city_list = re.compile('"cityurl":"(\w+?)"').findall(response.text)

    def get_url(self):
        url = 'http://hotel.qunar.com/city/hotelLocationCategory.jsp?cityurl=%s&_=%s'
        for hot_city in self.hot_city_list:
            yield url % (hot_city, int(time.time()))
        with open(r'cold_city.txt','r',encoding='utf-8') as f:
            cold_city_list = f.readlines()
        for cold_city in cold_city_list:
            if cold_city not in self.hot_city_list:
                yield url % (cold_city.replace('\n',''), int(time.time()))



    def get_cold_city(self):
        pass


if __name__ == '__main__':
    qnr = Qnr()
    city_list = qnr.get_url()
    for city in city_list:
        print(city)
