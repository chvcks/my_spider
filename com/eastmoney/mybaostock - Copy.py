# -*- coding:utf-8 -*-
'''
@author shilong
'''

import baostock as bs

import pandas as pd
import matplotlib.pyplot as plt

lg=bs.login()

#print('login respond error_code:'+lg.error_code)
#print('login respond  error_msg:'+lg.error_msg)

fields= "date,code,open,high,low,close"
rs = bs.query_history_k_data("sz.000831", fields,
    start_date='2019-01-01', end_date='2019-02-21',
    frequency="d", adjustflag="2")
#frequency="d"取日k线，adjustflag="3"默认不复权，
#1：后复权；2：前复权

data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)
result.index=pd.to_datetime(result.date)
#### 结果集输出到csv文件 ####
result.to_csv("gif/history_k_data.csv",
        encoding="gbk", index=False)
print(result)
result.head()
#### 登出系统 ####
#bs.logout()

result.info()

#将某些object转化numeric
result=result.apply(pd.to_numeric, errors='ignore')
result.info()

result.close.plot(figsize=(16,8))
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
#plt.show()

from pyecharts import Kline

y=list(result.loc[:,['open','close','low','high']].values)

x=list(result.index.strftime('%Y%m%d'))

kline = Kline("000831K线图",title_text_size=15)
kline.add("", x, y,is_datazoom_show=False,
         mark_line=["average"],
         mark_point=["max", "min"],
         mark_point_symbolsize=60,
         mark_line_valuedim=['highest', 'lowest'] )
kline.render("gif/000831_bao.gif")
kline


print()