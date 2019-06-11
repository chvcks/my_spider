
from urllib import request
import requests

import time
import logging
import re
import random
import pdfkit
from bs4 import BeautifulSoup
import os
import urllib
from lxml import etree
import unidecode
import json
import ast
import wget


class XMLY(object):
    def __init__(self):

        self.headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0",
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                        'Accept-Encoding': 'gzip, deflate, sdch, br',
                        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                        'Connection': 'keep-alive',
                        }

        self.session = requests.session()
        self.myurl = "https://m.ximalaya.com/ertong/{}/{}"

        self.myproxy = {'http':"192.168.255.49:8080", 'https':"192.168.255.49:8080"}

    def parse_download(self,url, parent_id, id):

        try:

            page = self.session.get(url, headers=self.headers)
            soup = BeautifulSoup(page.text, "lxml")

            # 正文
            body = soup.find_all("script")
            str2json =unidecode.unidecode(body[0].string)
            str2json = str2json[str2json.index("{"):len(str2json)-1]

            d2=json.loads(str2json)
            key='/ertong/{}/{}'.format(parent_id, id)

            #d2 = json.loads(str(d2[key]))
            #d2 =ast.literal_eval(str(d2[key]))
            d2 = d2[key]

            d2 = d2['trackInfo']

            title = d2['title']
            download_src=d2['src']
            print(title)
            print(download_src)
            wget.download(d2['src'], '1A\\'+d2['title']+'.m4a')

        except Exception as e:
            logging.error("解析错误", exc_info=True)


    def download(self, parent_id, start_id, end_id):

        try:

            for id in range(int(start_id), int(end_id)):
                myurl = self.myurl.format(parent_id, id)

                self.parse_download(myurl, parent_id, id)

                sleeper = random.randint(2, 3)
                time.sleep(sleeper)

        except Exception as e:
            print (e)

if __name__=="__main__":
    xmly = XMLY()

    parent_id = "14082645"      #1A
    start_id = "75440136"
    end_id = "75440527"


    xmly.download(parent_id, start_id, end_id)
