# -*- coding:utf-8 -*-
'''
@author shilong
'''

import baostock as bs

import pandas as pd
from pyecharts import Kline
import time
import random


class MyBaoStock(object):
    def __init__(self):
        self.start_date = '2019-01-01'
        self.end_date = ''

    def create(self, code):
        rsbasic = bs.query_stock_basic(code)

        if len(rsbasic.data) > 0:
            data_basic_list = []
            while (rsbasic.error_code == '0') & rsbasic.next():
                data_basic_list.append(rsbasic.get_row_data())
            result_basic = pd.DataFrame(data_basic_list, columns=rsbasic.fields)
            # print(result_basic.code)
            # print(result_basic.to_dict()['code_name'][0])

            fields = "date,code,open,high,low,close"
            rs = bs.query_history_k_data_plus(code, fields,
                                         start_date=self.start_date, end_date=self.end_date,
                                         frequency="d", adjustflag="2")
            # frequency="d"取日k线，adjustflag="3"默认不复权，
            # 1：后复权；2：前复权

            data_list = []
            while (rs.error_code == '0') & rs.next():
                # 获取一条记录，将记录合并在一起
                data_list.append(rs.get_row_data())
            result = pd.DataFrame(data_list, columns=rs.fields)
            result.index = pd.to_datetime(result.date)

            y = list(result.loc[:, ['open', 'close', 'low', 'high']].values)

            x = list(result.index.strftime('%Y%m%d'))

            kline = Kline(result_basic.to_dict()['code_name'][0], title_text_size=15)
            kline.add("", x, y, is_datazoom_show=False,
                      mark_line=["average"],
                      mark_point=["max", "min"],
                      mark_point_symbolsize=60,
                      mark_line_valuedim=['highest', 'lowest'])
            kline.render("baostock/%s.gif" % (code))
            kline
        else:
            print("empty ----> " + rsbasic.code)


if __name__ == "__main__":
    bs.login()
    myBaoStock = MyBaoStock()

    try:
        # for id in range(600000, 603999, 1):

        # for code in range(600000, 600001):
        # print(code)
        #    myBaoStock.create("sh."+str(code))

        # for id in range(000001, 000166, 1):
        # for id in range(000301, 000999, 1):
        # for id in range(001696, 002958, 1):
        # for id in range(300001, 300761, 1):
        #for code in range(600000, 603999):
        # for code in range(1, 300761):
        for code in range(603901, 603999):
            code_str = str(code)
            code_len = len(code_str)

            if code_len == 1:
                code_str = "sz.00000" + str(code)
            elif code_len == 2:
                code_str = "sz.0000" + str(code)
            elif code_len == 3:
                if code <= 166 or code >= 301:
                    code_str = "sz.000" + str(code)
            elif code_len == 4:
                if code >= 1696 and code <= 2958:
                    code_str = "sz.00" + str(code)
            #elif code_len == 5:
                #print()
                #print("sz.0" + str(code))
            elif code_len == 6:
                if code >= 300001 and code <= 300761:
                    code_str = "sz." + str(code)

                if code >= 600000 and code <= 601999:
                    code_str = "sh." + str(code)

                if code >= 603000 and code <= 603999:
                    code_str = "sh." + str(code)

            if len(code_str) == 9:
                #print(code_str)
                myBaoStock.create(code_str)

    except Exception as e:
        print(e)

    bs.logout()
