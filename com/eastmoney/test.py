import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

#for page in range(1,10):
#    print(page)

url = "%d  http://guba.eastmoney.com/news,300059,%d.html  %d" % (1, 2, 3)
#print(url)



print(ts.__version__)

ts.set_token('9abc1a21020cecbdf2e5adfdf164015feeb6c846fe80d2c5c3f8ac1f')

pro = ts.pro_api()

basic=pro.stock_basic(list_status='L')

pa=pro.daily(ts_code='000831.SZ', start_date='20190101',
               end_date='20190220')

from pyecharts import Kline
#from pyecharts.engine import create_default_environment
pa.index=pd.to_datetime(pa.trade_date)

pa=pa.sort_index()
y=list(pa.loc[:,['open','close','low','high']].values)

t=pa.index
x=list(t.strftime('%Y%m%d'))
kline = Kline("000831K线图",title_text_size=15)
kline.add("", x, y,is_datazoom_show=False,
         mark_line=["average"],
         mark_point=["max", "min"],
         mark_point_symbolsize=60,
         mark_line_valuedim=['highest', 'lowest'] )

# create_default_environment(filet_ype)
# file_type: 'html', 'svg', 'png', 'jpeg', 'gif' or 'pdf'
#env = create_default_environment('jpeg')
#env.render_chart_to_file(kline, path='line.jpeg')

kline.render("gif/000831.gif")
kline



