# -*- coding:utf-8 -*-

from urllib import request
import requests
import time
import random

class WMcheck(object):
    def __init__(self):
        self.checkheaders = {
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
            self.session.post(self.login_url, cookies=self.mycookies, data=postdata, headers=self.loginheaders)

            for cookieTmp in self.session.cookies:
                if cookieTmp.name == 'JSESSIONID':
                    JSESSIONIDValue = cookieTmp.value

            self.checkheaders['Cookie'] = 'JSESSIONID={}; qrParam=; signAddress=; empSuffix=; companyName=ALE+China; i18n_deflut=zh_CN; usernameTemp=shilong.han@shilong.han@alcatel-lucent.com; passwordTemp=24093913; JSESSIONID=2C87CADD9D1470FF05669DE0632E7405'.format(JSESSIONIDValue)
            self.checkheaders['Host'] = 'www.walkiemate.com'
            check_page = self.session.post(self.check_url, cookies= self.mycookies,  headers = self.checkheaders)
            print(check_page.text)
        except Exception as e:
            print (e)

if __name__=="__main__":
    sleeper = random.randint(100, 1000)
    #sleeper = random.randint(10, 11)
    print("sleep {}s".format(sleeper))
    time.sleep(sleeper)
    wm = WMcheck()
    wm.check()