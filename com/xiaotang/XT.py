
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

html_template = """ 
                <!DOCTYPE html> 
                <html lang="en"> 
                <head> 
                    <meta charset="UTF-8"> 
                </head> 
                <body> 
                {content} 
                </body> 
                </html>     
            """

class XTxieyi(object):
    def __init__(self):
        self.headers = {
            'Host': '101.251.111.151:3618',
            'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0",
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding':'gzip, deflate',
            'Upgrade-Insecure-Requests':'1',
            'Cache-Control':'max-age=0',
            'Cookie': 'ASP.NET_SessionId=hhgy4s45kry0vmfyqdjd5545',
            'Connection':'keep-alive'
            }

        self.session = requests.session()
        self.xieyi_url = "http://101.251.111.151:3618/projectmanage/print/fpq/xy.aspx?IM=1&projectId=257&protoId=24&ownerId={}"

        self.myproxy = {'http':"135.251.235.16:8080", 'https':"135.251.235.16:8080"}

    def parse_url_to_html(self,url, name):

        try:
            qr_url = 'http://101.251.111.151:3618/projectmanage/print/fpq/barcode.axd?type=QR&value={}'.format(url)
            resp = urllib.request.urlopen(qr_url)
            raw = resp.read()
            with open("./barcode.axd", 'wb') as fp:
                fp.write(raw)

            response = requests.get(url, proxies=self.myproxy, headers=self.headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            # 正文
            body = soup.find_all(class_="mainTable")
            # 标题
            title = ''
            titleList = soup.select("tr > td > span")
            for titleItem in titleList:
                if str(titleItem.string).__contains__("室"):
                    print(titleItem.string)
                    title = str(titleItem.string).strip() + '.pdf'
                    break


            if len(title)>5:
                print(title)
                html = ''
                for bodyItem in body:
                    html = html + str(bodyItem)

                html = html_template.format(content=html)
                html = html.encode("utf-8")
                with open(name, 'wb') as f:
                    f.write(html)
                return title

        except Exception as e:
            logging.error("解析错误", exc_info=True)

    def save_pdf(self, htmls, file_pdf):
        options = {
            'page-size': 'Letter',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'custom-header': [
                ('Accept-Encoding', 'gzip')
            ],
            'cookie': [
                ('cookie-name1', 'cookie-value1'),
                ('cookie-name2', 'cookie-value2'),
            ],
            'outline-depth': 10,
        }

        if file_pdf != None and len(file_pdf)>5:
            pdfkit.from_file(htmls, file_pdf, options=options)


    def download(self):

        try:
            #for id in range(43000, 45000, 1):
            #for id in range(43000, 31827, -1):
            #for id in range(31826, 11919, -1):
            for id in range(10000, 11919):
            #for id in range(42879, 42869, -1):
                print(id)
                myurl = self.xieyi_url.format(id)
                idhtml = '{}.html'.format(id)

                idpdf = self.parse_url_to_html(myurl, idhtml)
                self.save_pdf(idhtml, idpdf)

                sleeper = random.randint(2, 3)
                time.sleep(sleeper)

        except Exception as e:
            print (e)

if __name__=="__main__":
    xtXieyi = XTxieyi()
    xtXieyi.download()
