import os
import subprocess
from PIL import Image


def image_to_string(img):
    text = ''
    value = 50

    while text == '' and value > 10:
        tmp_img = 'tmp' + img
        image = Image.open(img)
        imageConvert = image.convert('P')
        imageConvertPoint = imageConvert.point(lambda x: 0 if x < value else 250, '1')
        imageConvertPoint.save(tmp_img)

        subprocess.check_output(r'D:\tools\Python\Tesseract-OCR\tesseract.exe '
                                + tmp_img + ' ' + tmp_img.split('.')[0], shell=True)

        with open(tmp_img.split('.')[0] + '.txt', 'r', encoding='UTF-8') as f:
            text = f.read().strip()

        os.remove(tmp_img.split('.')[0] + '.txt')
        os.remove(tmp_img)
        value = value - 30
    else:
        print("got the authcode: %s" %(text))

    return text



