# -*- coding:utf-8 -*-


from PyPDF2 import PdfFileReader, PdfFileWriter

import os

def split_pdf(infn, outfn):
    pdf_output = PdfFileWriter()
    with open(infn, 'rb')  as f:
		pdf_input = PdfFileReader(f)
	#页面数量
    page_count = pdf_input.getNumPages()
    print(page_count)
    # 将 pdf 前5页
    for i in range(5):
        pdf_output.addPage(pdf_input.getPage(i))
        with open(outfn, 'wb') as f:
		    pdf_output.write(f)

def merge_pdf(pdf_folder, outfn):
    """将多个文件合并为一个文件"""
    pdf_output = PdfFileWriter()
    #这里文件夹中只有pdf文件
    pdfs = os.listdur(os.path.join(pdf_folder))
    for infn in infnList:
        pdf_input = PdfFileReader(open(infn, 'rb'))
        # 获取 pdf 共用多少页
        page_count = pdf_input.getNumPages()
        print(page_count)
        for i in range(page_count):
            pdf_output.addPage(pdf_input.getPage(i))
    pdf_output.write(open(outfn, 'wb'))







