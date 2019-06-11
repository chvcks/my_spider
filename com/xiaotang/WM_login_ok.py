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
import requests
from bs4 import BeautifulSoup
import time
from lxml import etree
import authcode_reader
import json

class JDlogin(object):
    def __init__(self,un,pw):
        self.headers = {'User-Agent':"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
                        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                        'Accept-Encoding':'gzip, deflate, sdch',
                        'Accept-Language':'zh-CN,zh;q=0.8',
                        'Connection':'keep-alive',
                        }
        self.session = requests.session()
        self.login_url = "http://passport.jd.com/uc/login"
        self.post_url = "http://passport.jd.com/uc/loginService"
        self.auth_url = "https://passport.jd.com/uc/showAuthCode"
        self.un = un
        self.pw = pw

    def get_authcode(self,url):
        self.headers['Host'] = 'authcode.jd.com'
        self.headers['Referer'] = 'https://passport.jd.com/uc/login'
        response = self.session.get(url, headers = self.headers)
        with open('authcode.jpg','wb') as f:
            f.write(response.content)
        authcode = authcode_reader.image_to_string('authcode.jpg')
        #print(authcode)
        return authcode

    def get_info(self):
        '''获取登录相关参数'''
        try:
            page = self.session.get(self.login_url, headers = self.headers )
            soup = BeautifulSoup(page.text, "lxml")
            #print(soup.prettify())
            #print(type(soup.form))

            input_list = soup.select('.form input')

            for input_item in input_list:
                #print(input_item)
                pass

            #print(soup.title)
            #print(soup.title.string)
            #print(type(soup.title.string))
            #print(soup.head.contents)
            for head_content in soup.head.contents:
                #print(head_content)
                pass

            for head_child in soup.head.children:
                #print(head_child)
                pass

            for head_child in soup.head.descendants:
                #print(head_child)
                pass

            #print(soup.title.parents)
            #print(soup.select('.login-tab'))

            input_list = soup.select('form > input')
            #print(soup.select('input[id="loginname"]'))
            #print('='*60)

            for input_item in input_list:
                #print(input_item)
                pass

            #print(soup.select('input[id="pubKey"]')[0]['name'])

            data = {}
            data['uuid'] = soup.select('input[id="uuid"]')[0]['value']
            data['eid'] = soup.select('input[id="eid"]')[0]['value']
            data['fp'] = soup.select('input[id="sessionId"]')[0]['value']
            data['_t'] = soup.select('input[id="token"]')[0]['value']
            rstr = soup.select('input[id="pubKey"]')[0]['name']
            data[rstr] = soup.select('input[id="pubKey"]')[0]['value']
            acRequired = self.session.post(self.auth_url, data={'loginName':self.un}).text #返回({"verifycode":true})或({"verifycode":false})

            if 'true' in acRequired:
                #print ('need authcode, plz find it and fill in ')

                input_list = soup.select('img[id="JD_Verification1"]')
                #print('=' * 60)
                for input_item in input_list:
                    pass
                    #print(input_item)

                #acUrl = soup.select('.form img')[0]['src2']
                acUrl = soup.select('img[id="JD_Verification1"]')[0]['src']
                #print(acUrl)
                #print(str(int(time.time()*1000)))
                acUrl = 'http:{}&yys={}'.format(acUrl,str(int(time.time()*1000)))
                #print(acUrl)
                authcode = self.get_authcode(acUrl)
                data['authcode'] = authcode
            else:
                data['authcode'] = ''

        except Exception as e:
            print (e)
        finally:
            return data


    def login(self):
        
        postdata = self.get_info()
        postdata['loginname'] = self.un
        postdata['nloginpwd'] = self.pw
        postdata['loginpwd'] = self.pw
        try:
            self.headers['Host'] = 'passport.jd.com'
            self.headers['Origin'] = 'https://passport.jd.com'
            self.headers['X-Requested-With'] = 'XMLHttpRequest'
            login_page = self.session.post(self.post_url, data = postdata, headers = self.headers)
            login_result = json.loads(login_page.text[1:len(login_page.text)-1])
            print(login_result)
            #print (login_result.get('success'))  #若返回{“success”:”http://www.jd.com”}，说明登录成功
            return login_result.get('success')
        except Exception as e:
            print (e)

if __name__=="__main__":
    username = "xqrsadfsdfxx"#input("plz enter username:")
    password = "ddwdww"#input("plz enter password:")
    JD = JDlogin(username,password)
    isfailed = JD.login()
    print(isfailed)
    print(type(isfailed))
    while(isfailed == None):
        isfailed = JD.login()
        time.sleep(10)