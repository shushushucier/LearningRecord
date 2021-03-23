#!/usr/bin/python
# coding:utf-8
import os
import numpy as np
import cv2
import random

MAX_VALUE = 100

# 源目录
MyPath = 'E:\\learning\\programming\\machineLearning\\dataset\\cyclegan\\BCrop\\'
# 输出目录
OutPath = 'E:\\learning\\programming\\machineLearning\\dataset\\cyclegan\\NewBCrop\\'


def Contrast_and_Brightness(alpha, beta, img):
    blank = np.zeros(img.shape, img.dtype)
    # dst = alpha * img + beta * blank
    dst = cv2.addWeighted(img, alpha, blank, 1 - alpha, beta)
    return dst


def update(lightness, saturation, image):
    """
    用于修改图片的亮度和饱和度
    :param input_img_path: 图片路径
    :param output_img_path: 输出图片路径
    :param lightness: 亮度
    :param saturation: 饱和度
    """

    # 加载图片 读取彩色图像归一化且转换为浮点型
    # image = cv2.imread("E:\\learning\\programming\\machineLearning\\dataset\\cyclegan\\B\\3146.jpg", cv2.IMREAD_COLOR).astype(np.float32) / 255.0
    image = cv2.cvtColor(image, cv2.IMREAD_COLOR).astype(np.float32) / 255.0
    # 颜色空间转换 BGR转为HLS
    hlsImg = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)

    # 1.调整亮度（线性变换)
    hlsImg[:, :, 1] = (1.0 + lightness / float(MAX_VALUE)) * hlsImg[:, :, 1]
    hlsImg[:, :, 1][hlsImg[:, :, 1] > 1] = 1
    # 饱和度
    hlsImg[:, :, 2] = (1.0 + saturation / float(MAX_VALUE)) * hlsImg[:, :, 2]
    hlsImg[:, :, 2][hlsImg[:, :, 2] > 1] = 1
    # HLS2BGR
    lsImg = cv2.cvtColor(hlsImg, cv2.COLOR_HLS2BGR) * 255
    lsImg = lsImg.astype(np.uint8)
    # cv2.imwrite(output_img_path, lsImg)
    return lsImg


def green(out2):
    # 绿化
    height, width, n = out2.shape
    out3 = out2.copy()
    for i in range(height):
        for j in range(width):
            b = out2[i, j][0]
            g = out2[i, j][1]
            r = out2[i, j][2]
            # 计算新的图像中的RGB值
            B = int(0.1 * r + 0.56 * g + 0.3 * b)
            # G = int(0.347 * r + 0.683 * g + 0.167 * b)
            G = int(0.1 * r + 0.734 * g + 0.3 * b)
            R = int(0.1 * r + 0.734 * g + 0.18 * b)  # 约束图像像素值，防止溢出
            out3[i, j][0] = max(0, min(B, 255))
            out3[i, j][1] = max(0, min(G, 255))
            out3[i, j][2] = max(0, min(R, 255))
    return out3


def y1(image):
    image2 = update(-10, -70, image)
    return image2


def y2(image):
    img2 = Contrast_and_Brightness(0.5, 0.2, image)
    return img2


def black1(image):
    image2 = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    image2 = cv2.cvtColor(image2, cv2.COLOR_GRAY2RGB)
    return image2


def black2(image):
    image2 = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    image2 = Contrast_and_Brightness(1, -70, image2)
    image2 = cv2.cvtColor(image2, cv2.COLOR_GRAY2RGB)
    return image2


def green1(image):
    img2 = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    img2 = Contrast_and_Brightness(1, -70, img2)
    img2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2RGB)
    img2 = green(img2)
    img2 = Contrast_and_Brightness(0.6, 20, img2)
    return img2


def operation(image):
    rand = random.randint(1, 6)
    if rand == 1:
        image = y1(image)
    elif rand == 2:
        image = y2(image)
    elif rand == 3:
        image = black1(image)
    elif rand == 4:
        image = black2(image)
    elif rand == 5:
        image = green1(image)
    elif rand == 6:
        pass
    return image


def processImage(filesoure, destsoure, name):
    im = cv2.imread(filesoure + name)
    im2 = operation(im)
    cv2.imwrite(destsoure + name, im2)


def run():
    os.chdir(MyPath)
    for i in os.listdir(os.getcwd()):
        # 检查后缀
        # postfix = os.path.splitext(i)[1]
        # if postfix == '.jpg' or postfix == '.png':
        processImage(MyPath, OutPath, i)
        print("--------------" + i + "----------------")


if __name__ == '__main__':
    run()
