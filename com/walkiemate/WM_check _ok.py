# -*- coding:utf-8 -*-
'''
Required
- requests
- bs4
Info
- author : "huangfs"
- email : "huangfs@bupt.edu.cn"
- date : "2016.4.13"
'''
from urllib import request
import requests
import json
from http import cookiejar

import time
import random

class WMcheck(object):
    def __init__(self):
        self.headers = {
            #'Host':'www.walkiemate.com',
            'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0",
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding':'gzip, deflate, br',
            #'Cookie':'JSESSIONID=C6ADDC2A71BECFAC1F10F010659B8B9E; qrParam=; signAddress=; empSuffix=; companyName=ALE+China; i18n_deflut=zh_CN; usernameTemp=shilong.han@shilong.han@alcatel-lucent.com; passwordTemp=24093913; JSESSIONID=2C87CADD9D1470FF05669DE0632E7405',
            'Upgrade-Insecure-Requests':'1',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive'
            }

        self.loginheaders = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0",
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '103',
            'Upgrade-Insecure-Requests': '1',
            'Connection': 'keep-alive'
        }
        self.session = requests.session()
        self.check_url = "https://www.walkiemate.com/hr_communication/EmpInfoAction.do?method=CheckByPerson"
        self.login_url2 = "https://www.walkiemate.com/hr_communication/login.jsp"
        self.login_url = "https://www.walkiemate.com/hr_communication/LoginAction.do?method=login"

        self.mycookies = dict(
            JSESSIONID='2C87CADD9D1470FF05669DE0632E7405',
            companyName='ALE+China',
            empSuffix='',
            i18n_deflut='zh_CN',
            passwordTemp='24093913',
            qrParam='',
            signAddress=''
        )



    def check(self):

        try:
            postdata = {}
            postdata['username'] = 'shilong.han@alcatel-lucent.com'
            postdata['empSuffix'] = ''
            postdata['password'] = '24093913'
            postdata['check'] = ''
            postdata['language'] = 'zh_CN'
            postdata['forwardTo'] = ''
            login_page = self.session.post(self.login_url, cookies=self.mycookies, data=postdata, headers=self.loginheaders)
            #print(login_page.text)


            for cookieTmp in self.session.cookies:
                if cookieTmp.name == 'JSESSIONID':
                    JSESSIONIDValue = cookieTmp.value
                    print(cookieTmp.value)

            cookie = cookiejar.CookieJar()
            handler = request.HTTPCookieProcessor(cookie)
            request.build_opener(handler).open(self.login_url)
            for cookieTmp in cookie:
                if cookieTmp.name == 'JSESSIONID':
                    #JSESSIONIDValue = cookieTmp.value
                    print(cookieTmp.value)

            cookie2 = cookiejar.CookieJar()
            handler2 = request.HTTPCookieProcessor(cookie2)
            request.build_opener(handler2).open(self.login_url2)
            for cookieTmp in cookie2:
                if cookieTmp.name == 'JSESSIONID':
                    #JSESSIONIDValue = cookieTmp.value
                    print(cookieTmp.value)

            cookie3 = cookiejar.CookieJar()
            handler3 = request.HTTPCookieProcessor(cookie3)
            request.build_opener(handler3).open(self.check_url)
            for cookieTmp in cookie3:
                if cookieTmp.name == 'JSESSIONID':
                    #JSESSIONIDValue = cookieTmp.value
                    print(cookieTmp.value)

            self.headers['Cookie'] = 'JSESSIONID={}; qrParam=; signAddress=; empSuffix=; companyName=ALE+China; i18n_deflut=zh_CN; usernameTemp=shilong.han@shilong.han@alcatel-lucent.com; passwordTemp=24093913; JSESSIONID=2C87CADD9D1470FF05669DE0632E7405'.format(JSESSIONIDValue)
            #self.headers['Cookie'] = 'qrParam=; signAddress=; empSuffix=; companyName=ALE+China; i18n_deflut=zh_CN; usernameTemp=shilong.han@shilong.han@alcatel-lucent.com; passwordTemp=24093913; JSESSIONID=2C87CADD9D1470FF05669DE0632E7405'
            self.headers['Host'] = 'www.walkiemate.com'
            print(self.headers['Cookie'])
            check_page = self.session.post(self.check_url, cookies= self.mycookies,  headers = self.headers)
            #print (check_page.__getattribute__('cookies'))


            #self.headers['Cookie'] = 'JSESSIONID={}; qrParam=; signAddress=; empSuffix=; companyName=ALE+China; i18n_deflut=zh_CN; usernameTemp=shilong.han@shilong.han@alcatel-lucent.com; passwordTemp=24093913; JSESSIONID=2C87CADD9D1470FF05669DE0632E7405'.format(JSESSIONIDValue)
            #check_page = requests.get(self.check_url, cookies=self.mycookies, headers=self.headers)
            print(check_page.text)
        except Exception as e:
            print (e)

if __name__=="__main__":
    wm = WMcheck()
    wm.check()
    sleeper = random.randint(100, 1000)
    print(sleeper)