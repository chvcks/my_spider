# !/usr/bin/python3

for n in range(2, 10):
    # print(n)
    for x in range(2, n):
        # print('x=', x, ', n=', n)
        if n % x == 0:
            # print(n, '=', x, '*', n // x)
            break
    else:
        print(n, 'is zhishu')


def printinfo(arg1, *others):
    print(arg1)
    for other in others:
        print(other)
    return


printinfo(10)
printinfo('-------')
printinfo(10, 23, 33, 'ee', 44, 55, 67, 8)

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(20)
y = x ** 2

plt.plot(x, y)

from urllib.request import urlopen

with urlopen('https://docs.python.org/3/tutorial/stdlib.html') as response:
    for line in response:
        line = line.decode('utf-8')
        # print(line)
        if 'EST' in line or 'EDT' in line:
            print(line)

import smtplib

'''
server = smtplib.SMTP('localhost')
server.sendmail('shilong.han@al-enterprise.com', '13524436977@163.com',
                
                TO: 13524436977@163.com
                From: shilong.han@al-enterprise.com
                
                Beware the Ides of March.
                
                )
server.quit()
'''

from datetime import date

now = date.today()
print(now)
print(now.strftime('%m-%d-%y  %d %b %Y is a %A on the %d day of %B'))

brithday = date(2010, 9, 18)
age = now - brithday
print(age.days)


def average(values):
    '''
    computes the arithmetic mean of a list of numbers.

    :param values:
    :return:
    '''
    return sum(values) / len(values)


import doctest

doctest.testmod()

import unittest


class TestStatisticalFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)

        with self.assertRaises(ZeroDivisionError):
            self.average = average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)


#unittest.main()
import textwrap
doc = '''  The wrap() method is just like fill() except that it returns a list of strings instead of one big string with newlines to separate the wrapped lines.'''
print(textwrap.fill(doc, width=40))
print(doc)

import threading, zipfile
class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile  = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('test.txt', 'test.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')

import reprlib
print(reprlib.repr(set('aaaaaaaaaaa')))

from string import Template
t = Template('${village} folk send $$10 to $cause.')
t.substitute(village= 'nottingham', cause='the dict fund')
print(str(t))

#fmt = input('Enter rename style (%d-date)')

import struct
with open('test.zip', 'rb') as f:
    data = f.read()

print(data)
'''
start = 0
for i in range(3):
    start += 14
    fields = struct.unpack('<IIIHH', data[start: start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start + filenamesize]
    start += filenamesize
    extra = data[start:start + extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size
'''
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')

from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
print(data)
heapify(data)
print(data)
heappush(data, -5)
print(data)
print(heappop(data))
print(data)
print(heappop(data))
print(data)

from decimal import *
print(round(Decimal('0.70') * Decimal('1.05'), 2))
print(round(Decimal('0.70') * Decimal('1.05'), 4))
print(round(.70 * 1.05, 2))
print(round(.70 * 1.05, 4))






















