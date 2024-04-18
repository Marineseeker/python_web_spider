import os
import pytesseract
from PIL import Image
import numpy as np


def Grey_release_treatment(image):
    image = image.convert('L')
    threshold = 150
    array = np.array(image)
    array = np.where(array > threshold, 255, 50)
    image = Image.fromarray(array.astype('uint8'))
    return image

# 定义图像文件夹路径
folder_path = 'pythonproject/request/selenium/Pixpin'

# 遍历文件夹内所有图片文件
for filename in os.listdir(folder_path):
    if filename.endswith(('.png')):
        # 构建图像文件的完整路径
        image_path = os.path.join(folder_path, filename)
        try:
            # 打开图像文件
            image = Image.open(image_path)
            image = Grey_release_treatment(image)
            # 使用 pytesseract 进行 OCR
            text = pytesseract.image_to_string(image)
            if text:
                # 打印识别的文本
                print(f"文件名: {filename}, 识别结果: {text}")
            else:
                print(f"文件名: {filename}, 识别结果: 什么也没有, \n")
        except Exception as e:
            print(f"文件名: {filename}, 错误: {e}")
