# -*- coding:utf-8 -*-
'''
@author shilong
'''
import requests
from bs4 import BeautifulSoup
import time
from lxml import etree
import authcode_reader
import json
import re
import threading

class JDMonitor(threading.Thread):
    def __init__(self, product_id, expected_price):
        self.headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0",
                        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                        'Accept-Encoding':'gzip, deflate, sdch, br',
                        'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                        'Connection':'keep-alive',
                        }
        self.session = requests.session()
        #self.priceUrl = 'http://p.3.cn/prices/mgets?skuIds=%(skuIds)s&type=%(type)s'
        #'https://p.3.cn/prices/mgets?pduid=15246223326421079810333&skuIds=J_8066717'
        self.priceUrl = 'https://p.3.cn/prices/mgets?pduid=%(pduid)s&skuIds=%(skuIds)s&type=%(type)s'
        self.productUrl = 'https://item.jd.com/{}.html'.format(product_id)
        self.expectedPrice = expected_price
        threading.Thread.__init__(self)

    def getInfo(self):
        try:
            page = self.session.get(self.productUrl, headers = self.headers )
            soup = BeautifulSoup(page.text, "lxml")

            data = {}
            for span_item in soup.find_all('span', class_='p-price'):
                data['type'] = 1
                data['pduid'] = int(time.time())
                data['skuIds'] = re.compile(r'\d+').findall(repr(span_item))[0]
                break
        except Exception as e:
            print (e)
        finally:
            return data

    def getPrice(self):
        getInfo = self.getInfo()
        try:
            self.priceUrl = self.priceUrl % getInfo
            price_page = self.session.get(self.priceUrl)

            return price_page.json()[0]['p']
        except Exception as e:
            print (e)



    def run(self):
        try:
            while float(self.getPrice()) > self.expectedPrice:
                price = float(self.getPrice())
                print("The latest price of {} IS: {}, while expected price IS: {}".format(self.productUrl, self.getPrice(), self.expectedPrice))
                time.sleep(10)
            else:
                print("!!!The latest price of {} IS: {}, buy it now !!!".format(self.productUrl, self.getPrice()))

        except Exception as e:
            print (e)

if __name__=="__main__":

    productDict = {
                   "1682719":30,
                   "3444627":2500,
                   "8066717":2699
                   }

    for product in productDict.items():
        JDMonitor(product[0], product[1]).start()


