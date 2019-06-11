# -*- coding:utf-8 -*-
'''
@author shilong
'''
import requests
from bs4 import BeautifulSoup
import time
from lxml import etree
import sys
sys.path.append("..")
from jd import authcode_reader
import json
import re
import threading

class StationName:
    def __init__(self, file_name):
        self.headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0",
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                        'Accept-Encoding': 'gzip, deflate, sdch, br',
                        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                        'Connection': 'keep-alive',
                        }
        self.session = requests.session()
        self.fileName = file_name
        self.fileJson = "name_code.json"
        self.url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9061'

    def getStationNameAndSave(self):
        resp = self.session.get(self.url, headers=self.headers)
        if resp.status_code == 200:
            print('station_name_code():获取站点信息成功!')
            with open(self.fileName, 'w') as f:
                for each in resp.text.split('=')[1].split('@'):
                    if each != "'":
                        #print(each)
                        f.write(each)
                        f.write('\n')
        else:
            print('station_name_code() error! status_code:{}, url: {}'
                  .format(resp.status_code, resp.url))

        self.saveStationCode()

    def saveStationCode(self):
        name_code_dict = {}
        with open(self.fileName, 'r') as f:
            for line in f:
                # 对读取的行都进行split操作,然后提取站点名和其代码
                name = line.split('|')[1] # 站点名字
                code = line.split('|')[2] # 每个站点对应的代码
                # 每个站点肯定都是唯一的
                name_code_dict[name] = code

        # 把name,code保存到本地文件中,方便以后使用
        with open(self.fileJson, 'w') as f:
            # 不以ascii码编码的方式保存
            json.dump(name_code_dict, f, ensure_ascii=False)


if __name__=="__main__":
    StationName("station_name.txt").getStationNameAndSave()