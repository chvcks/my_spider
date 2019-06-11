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
            '半年度过渡费',
            '搬家补助',
            '奖励费',
            '速迁奖',
            '租房补贴',
            '其他',
            '合计',
            '合同生成日期',
            '链接']


        self.xieyi_url = "http://101.251.111.151:3618/projectmanage/print/fpq/xy.aspx?IM=1&projectId=257&protoId=24&ownerId={}"


    def download(self):

        try:
            wb = openpyxl.Workbook()
            sheet = wb.active

            for i in range(len(self.headList)):
                sheet['{}1'.format(self.alphaList[i])] = self.headList[i]

            allhtmls = [f for f in os.listdir('./html') if os.path.isfile(os.path.join('./html', f))]

            for j in range(len(allhtmls)):
                currentFileName = r'html/' + allhtmls[j]
                soup = BeautifulSoup(open(currentFileName,'r',encoding="utf8"), 'html.parser')

                total = None
                trtdspanList = soup.select("tr > td > span")
                for item in trtdspanList:
                    if str(item.string).__contains__("室"):
                        address = str(item.string).strip()
                        mianji = str(item.next_sibling.next_sibling.string).strip()
                    elif str(item.parent).__contains__("合计人民币") and not total:
                        total = str(item.string).strip()


                loucengchajia = None
                jiangli = None
                zufang = None

                trtdinputList = soup.select("tr > td > input")
                for item in trtdinputList:
                    if str(item.parent).__contains__("乙　　方"):
                        name = str(item.get('value')).strip()
                    elif str(item.parent).__contains__("装潢"):
                        zhuangxiu = str(item.get('value')).strip()
                    elif str(item.parent).__contains__("楼层差价"):
                        if not loucengchajia:
                            loucengchajia = str(item.get('value')).strip()
                        else:
                            loucengchajiaall = str(item.get('value')).strip()
                    elif str(item.parent).__contains__("半年度过渡费"):
                        halfyear = str(item.get('value')).strip()
                    elif str(item.parent).__contains__("搬家补助费"):
                        banjia = str(item.get('value')).strip()
                    elif str(item.parent).__contains__("奖励费"):
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
                    if str(item.string).__contains__("秒"):
                        checkdate = str(item.string).strip()

                linkaddress = self.xieyi_url.format(allhtmls[j][0:-5])

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
                            checkdate,
                            linkaddress]

                print(datalist)
                for i in range(len(datalist)):
                    sheet[self.alphaList[i] + str(j+2)] = datalist[i]

            wb.save('all.xlsx')

        except Exception as e:
            print (e)

if __name__=="__main__":
    xtXieyi = XTxieyi()
    xtXieyi.download()
