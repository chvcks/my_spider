#from login import Login
import os
import json
import time
from collections import deque, OrderedDict
import requests
from bs4 import BeautifulSoup
from bs4 import Tag
from bs4 import NavigableString

from lxml import etree
import sys
sys.path.append("..")
from jd import authcode_reader

import re
import threading

class Eastmoney(threading.Thread):
    """ 查询车票信息 """

    def __init__(self, maxPage, sleepTime):
        self.headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0",
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                        'Accept-Encoding': 'gzip, deflate, sdch, br',
                        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                        'Connection': 'keep-alive',
                        }
        self.pageUrl = "http://guba.eastmoney.com/list,300059_%d.html"
        self.tieziUrl = "http://guba.eastmoney.com/news,300059,%(tiezi)s.html"
        self.session = requests.session()
        self.maxPage = maxPage + 1
        self.sleepTime = sleepTime
        threading.Thread.__init__(self)

    def run(self):
        try:
            while True:

                print("="*10+"最热门的10个帖子是："+"="*10)
                self.getTop10Web()
                time.sleep(self.sleepTime)
            else:
                print("never run")

        except Exception as e:
            print(e)

    def getTop10(self):
        try:
            data = []
            for page in range(1, self.maxPage):
                tempPgeUrl = self.pageUrl % page
                #print(tempPgeUrl)

                pageContent = self.session.get(tempPgeUrl, headers=self.headers)
                soup = BeautifulSoup(pageContent.text, "lxml")

                for div_item in soup.find_all('div', class_='articleh'):
                    isSkip = False
                    countBrowsed = 0
                    tieziId = 0
                    wroteDate = ''
                    #print(div_item)

                    for child in div_item.descendants:
                        if child.name == 'em':
                            isSkip = True
                            continue
                            
                        if isinstance(child, Tag) and child.get('class') != None:
                            if child.get('class')[0] == 'l1':
                                countBrowsed = child.string
                            elif child.get('class')[0] == 'l3':
                                hrefStr = re.split('[,.]', str(child.find('a').get('href')))
                                tieziId = hrefStr[2]
                            elif child.get('class')[0] == 'l6':
                                wroteDate = child.string


                    if isSkip == False and isinstance(countBrowsed, NavigableString):
                        data.append((int(countBrowsed), tieziId, wroteDate))
                        #print(type(countBrowsed))
                        #print(div_item)
                        #pass


        except Exception as e:
            print (e)
        finally:
            data.sort(reverse=True)
            return data[5:15]

    def getTop10Web(self):
        top10List = self.getTop10()
        #print(top10List)
        print("=====人气=====    ========================帖子========================  ====发布日期====")
        for top10Item in top10List:
            print("====%d====    http://guba.eastmoney.com/news,300059,%s.html    ====%s====" % (top10Item[0], top10Item[1], top10Item[2]))




if __name__ == '__main__':
    Eastmoney(2, 10).start()
    #Eastmoney(1, 10).getTop10()