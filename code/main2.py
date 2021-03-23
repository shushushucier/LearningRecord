#!/usr/bin/python
# coding:utf-8
import os
import numpy as np
import cv2
import random

# 源目录
MyPath = 'E:\\learning\\programming\\machineLearning\\dataset\\cyclegan\\data1\\yellow\\onlyYellow\\testB\\'
# 输出目录
OutPath = 'E:\\learning\\programming\\machineLearning\\dataset\\cyclegan\\B\\'


def GaussianNoise(src, means, sigma):
    NoiseImg = src
    # rows = NoiseImg.shape[0]
    # cols = NoiseImg.shape[1]
    rows, cols, n = NoiseImg.shape
    for i in range(rows):
        for j in range(cols):
            NoiseImg[i, j][0] = NoiseImg[i, j][0] + random.gauss(means, sigma)
            NoiseImg[i, j][1] = NoiseImg[i, j][1] + random.gauss(means, sigma)
            NoiseImg[i, j][2] = NoiseImg[i, j][2] + random.gauss(means, sigma)
            for k in range(0, 2):
                if NoiseImg[i, j][k] < 0:
                    NoiseImg[i, j][k] = 0
                elif NoiseImg[i, j][k] > 255:
                    NoiseImg[i, j][k] = 255
    return NoiseImg


def gasuss_noise(image, mean, var):
    """
        添加高斯噪声
        mean : 均值
        var : 方差
    """
    image = np.array(image / 255, dtype=float)
    noise = np.random.normal(mean, var ** 0.5, image.shape)
    out = image + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out * 255)
    return out


def processImage(filesoure, destsoure, name):
    """
     filesoure是存放待转换图片的目录
     destsoure是存在输出转换后图片的目录
     name是文件名
     imgtype是文件类型
     """
    # 打开图片
    # im = Image.open(filesoure + name)
    im = cv2.imread(filesoure + name)
    im2 = GaussianNoise(im, 0, 0.01)
    im3 = gasuss_noise(im, 0, 0.0001)
    # cv2.imwrite(destsoure + name, im2)
    cv2.imshow("aa", im2)
    cv2.imshow("bb", im3)
    cv2.waitKey()


def run():
    # 切换到源目录，遍历源目录下所有图片
    os.chdir(MyPath)
    for i in os.listdir(os.getcwd()):
        # 检查后缀
        # postfix = os.path.splitext(i)[1]
        # if postfix == '.jpg' or postfix == '.png':
        processImage(MyPath, OutPath, i)
        print("--------------" + i + "----------------")


if __name__ == '__main__':
    processImage(MyPath, OutPath, '1.jpg')

