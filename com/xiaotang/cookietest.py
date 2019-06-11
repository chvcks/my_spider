from urllib import request
from http import cookiejar

import requests
import json

cookie = cookiejar.MozillaCookieJar()

with open('cookies.json') as f:
    cookiedata = json.load(f)

#print(cookiedata['cookies'][1]['value'])
#cookie.load(json.dumps(cookiedata),ignore_discard=True, ignore_expires=True)

cookie2 = cookiejar.CookieJar()
handler = request.HTTPCookieProcessor(cookie2)
opener = request.build_opener(handler)

login_url = "https://www.walkiemate.com/hr_communication/LoginAction.do?method=login"

check_url = "https://www.walkiemate.com/hr_communication/EmpInfoAction.do?method=CheckByPerson"
response = opener.open('https://www.walkiemate.com/hr_communication/login.jsp')
#print(cookie2[0].value)
for cookieTmp in cookie2:
    print(cookieTmp.name)
    print(cookieTmp.value)

#response = opener.open('http://172.24.190.221/index.pl/')
mycookies = dict(
                 JSESSIONID='2C87CADD9D1470FF05669DE0632E7405',
                 companyName='ALE+China',
                 empSuffix='',
                 i18n_deflut='zh_CN',
                 passwordTemp='24093913',
                 qrParam='',
                 signAddress=''
                 )
#print(mycookies)

myheaders = {
            'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0",
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding':'gzip, deflate, br',
            'Content-Type':'application/x-www-form-urlencoded',
            'Content-Length':'103',
            'Upgrade-Insecure-Requests':'1',
            'Connection':'keep-alive'
            }

checkheaders = {
            'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0",
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding':'gzip, deflate, br',
            'Content-Type':'application/x-www-form-urlencoded',
            'Content-Length':'0',
            'Pragma':'no-cache',
            'Cache-Control':'no-cache',
            'X-Requested-With':'XMLHttpRequest',
            'Connection':'keep-alive'
            }

checkheaders2 = {
            'Host':'www.walkiemate.com',
            'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0",
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding':'gzip, deflate, br',
            'Cookie':'JSESSIONID=8E379E2E90B3C62EA243F232EB233D2E; qrParam=; signAddress=; empSuffix=; companyName=ALE+China; i18n_deflut=zh_CN; usernameTemp=shilong.han@shilong.han@alcatel-lucent.com; passwordTemp=24093913; JSESSIONID=2C87CADD9D1470FF05669DE0632E7405',
            'Upgrade-Insecure-Requests':'1',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive'
            }
session = requests.session()
postdata = {}
postdata['username'] = 'shilong.han@alcatel-lucent.com'#cookiedata['cookies'][1]['value']
postdata['empSuffix'] = ''#cookiedata['cookies'][6]['value']
postdata['password'] = '24093913'#cookiedata['cookies'][2]['value']
postdata['check'] = ''#cookiedata['cookies'][6]['value']
postdata['language'] = 'zh_CN'#cookiedata['cookies'][0]['value']
postdata['forwardTo'] = ''

login_page1 =session.post(login_url, cookies= mycookies,  data = postdata, headers = myheaders)
#print (login_page1.text)

#login_page =requests.post(login_url, cookies= mycookies,  data = postdata, headers = myheaders)
#print (login_page.text)

check_page =session.post(check_url, cookies= mycookies,  headers = checkheaders2)
print (check_page.text)

#response = requests.post().get(login_url, headers = myheaders, cookies = cookie)
#response = opener.open(login_url)
#for item in cookie:
#    print('Name = %s, Value = %s' %(item.name, item.value))
