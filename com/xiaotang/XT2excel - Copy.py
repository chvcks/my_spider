# -*- coding:utf8 -*-
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
import openpyxl
import codecs

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

        self.alphaList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
        self.headList = [
            '文件名',
            '户主',
            '产证面积',
            '装潢及附属设施',
            '楼层差价',
            '补偿金额',
            '半年度过渡费', '搬家补助',
            '奖励费', '速迁奖',
            '租房补贴', '其他',
            '合计', '合同生成日期',
            '链接']


        self.xieyi_url = "http://101.251.111.151:3618/projectmanage/print/fpq/xy.aspx?IM=1&projectId=257&protoId=24&ownerId={}"


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
            wb = openpyxl.Workbook()
            sheet = wb.active

            for i in range(14):
                sheet['{}1'.format(self.alphaList[i])] = self.headList[i]

            allhtmls = [f for f in os.listdir('./html') if os.path.isfile(os.path.join('./html', f))]
            print(allhtmls)

            for j in range(len(allhtmls)):
                print(allhtmls[j])
                currentFileName = r'html/' + allhtmls[j]
                soup = BeautifulSoup(open(r'html/31222.html','r',encoding="utf8"), 'html.parser')

                total = None
                trtdspanList = soup.select("tr > td > span")
                for item in trtdspanList:
                    #print(item)
                    if str(item.string).__contains__("室"):
                        address = str(item.string).strip()
                        mianji = str(item.next_sibling.next_sibling.string).strip()
                    elif str(item.parent).__contains__("合计人民币") and not total:
                        #print(item.string)
                        total = str(item.string).strip()


                loucengchajia = None
                jiangli = None
                zufang = None

                trtdinputList = soup.select("tr > td > input")
                for item in trtdinputList:
                    #print(str(item.parent))
                    #print(type(item.parent))
                    #print(item)
                    if str(item.parent).__contains__("乙　　方"):
                        #print(item)
                        name = str(item.get('value')).strip()
                    elif str(item.parent).__contains__("装潢"):
                        #print(item)
                        zhuangxiu = str(item.get('value')).strip()
                    elif str(item.parent).__contains__("楼层差价"):
                        if not loucengchajia:
                            loucengchajia = str(item.get('value')).strip()
                        else:
                            loucengchajiaall = str(item.get('value')).strip()
                    elif str(item.parent).__contains__("半年度过渡费"):
                        #print(item)
                        halfyear = str(item.get('value')).strip()
                    elif str(item.parent).__contains__("搬家补助费"):
                        #print(item)
                        banjia = str(item.get('value')).strip()
                    elif str(item.parent).__contains__("速迁奖"):
                        if not jiangli:
                            jiangli = str(item.get('value')).strip()
                        else:
                            suqianjiang = str(item.get('value')).strip()
                    elif str(item.parent).__contains__("其他"):
                        if not zufang:
                            zufang = str(item.get('value')).strip()
                        else:
                            others = str(item.get('value')).strip()



                trtdList = soup.select("tr > td")
                for item in trtdList:
                    # print(item)
                    if str(item.string).__contains__("秒"):
                        checkdate = str(item.string).strip()

                linkaddress = self.xieyi_url.format('31222.html')

                datalist = [address,
                            name,
                            mianji,
                            zhuangxiu,
                            loucengchajia,
                            loucengchajiaall,
                            halfyear,
                            banjia,
                            jiangli,
                            suqianjiang,
                            zufang,
                            others,
                            total,
                            checkdate]

            for i in range(14):
                sheet['{}2'.format(self.alphaList[i])] = datalist[i]

            '''
            print(address)
            print(name)
            print(mianji)
            print(zhuangxiu)
            print(loucengchajia)
            print(loucengchajiaall)
            print(halfyear)
            print(banjia)
            print(jiangli)
            print(suqianjiang)
            print(zufang)
            print(others)
            print(total)
            print(checkdate)
            '''


            wb.save('all.xlsx')

        except Exception as e:
            print (e)

if __name__=="__main__":
    xtXieyi = XTxieyi()
    xtXieyi.download()
