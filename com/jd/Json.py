# -*- coding=utf-8 -*-
import urllib.request
import json
import requests

param1 = 'skuIds'
param2 = 'type'
params = {"skuIds": "J_5853579", "type": "1"}
#http://p.3.cn/prices/mgets?skuIds=J_1682719&type=1
fullUrl = 'http://p.3.cn/prices/mgets?skuIds=J_1682719&type=1'
apiUrl = 'http://p.3.cn/prices/mgets?'
formatUrl = 'http://p.3.cn/prices/mgets?skuIds=%(skuIds)s&type=%(type)s'
jParams = json.dumps(params)
print(jParams)
print(formatUrl % params)
headers = {'Content-Type': 'application/json'} # 设置数据为json格式，很重要
request = urllib.request.Request(url=apiUrl, headers=headers, data=jParams)
request2 = requests.get(fullUrl).json()
print(request2)
print(request2[0]['p'])
#response = urllib.request.urlopen(request)
#print (response.getcode()) # 请求状态，200为成功
#print (response.read()) # 返回的body