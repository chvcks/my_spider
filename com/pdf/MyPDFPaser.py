# -*- coding: utf-8 -*-
"""
目标：从pdf文件中抽取出含有关键字的页面，并将这些页面合并一个新的pdf文件
"""
from PyPDF2 import PdfFileReader, PdfFileWriter
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfparser import PDFDocument
from pdfminer.pdfparser import PDFPage
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import *
from pdfminer.converter import PDFPageAggregator

import re
import os

fp = open('P020180726534747201840.pdf', 'rb')

# 来创建一个pdf文档分析器
parser = PDFParser(fp)

# 创建一个PDF文档对象存储文档结构
document = PDFDocument()
parser.set_document(document)
document.set_parser(parser)
document.initialize('')

# 创建一个PDF资源管理器对象来存储共赏资源
rsrcmgr = PDFResourceManager()

# 设定参数进行分析
laparams = LAParams()
laparams.char_margin = 1.0
laparams.word_margin = 1.0

# 创建一个PDF设备对象
# device=PDFDevice(rsrcmgr)
device = PDFPageAggregator(rsrcmgr, laparams=laparams)

# 创建一个PDF解释器对象
interpreter = PDFPageInterpreter(rsrcmgr, device)

extracted_text = ''

for page in document.get_pages():
    interpreter.process_page(page)

    # # 接受该页面的LTPage对象
    layout = device.get_result()  # return text image line curve
    for x in layout:
        if isinstance(x, LTText) or isinstance(x, LTTextBox) or isinstance(x, LTTextLine):
            if x.get_text().__contains__("实际控制人"):
                print(x.get_text())
                extracted_text += x.get_text()

with open('pdf_result.txt', "wb") as txt_file:
    txt_file.write(extracted_text.encode("utf-8"))

fp.close()
