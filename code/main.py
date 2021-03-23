#!/usr/bin/python
# coding:utf-8
import os
import numpy as np
import cv2
import random

# 源目录
MyPath = 'E:\\learning\\dachuang\\cyclegan\\carDS\\complete\\final\\scratchB\\train\\'
# 输出目录
OutPath = 'E:\\learning\\dachuang\\cyclegan\\carDS\\complete\\final\\scratchBmohu\\train\\'


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


def gasuss_blur(out, k, ran3):
    # 高斯模糊
    out2 = cv2.GaussianBlur(out, (k, k), ran3)
    return out2


def yellowing(out2):
    # 黄化1
    height, width, n = out2.shape
    out3 = out2.copy()
    for i in range(height):
        for j in range(width):
            b = out2[i, j][0]
            g = out2[i, j][1]
            r = out2[i, j][2]
            # 计算新的图像中的RGB值
            B = int(0.273 * r + 0.535 * g + 0.131 * b)
            G = int(0.347 * r + 0.683 * g + 0.167 * b)
            R = int(0.395 * r + 0.763 * g + 0.188 * b)  # 约束图像像素值，防止溢出
            out3[i, j][0] = max(0, min(B, 255))
            out3[i, j][1] = max(0, min(G, 255))
            out3[i, j][2] = max(0, min(R, 255))
    # cv2.imshow("gasuss", out3)
    # cv2.waitKey(0)
    return out3


def operation(image1):
    # mean = 0
    # k = 0
    # var = random.uniform(5, 50)
    # rand1 = random.randint(1, 10)
    # rand2 = random.randint(1, 10)
    # if rand1 > 3:
    #     # out = gasuss_noise(image1, mean, var)
    #     out = GaussianNoise(image1, mean, var)
    # ran2 = random.randint(0, 2)
    # ran3 = random.randint(1, 5)
    # if ran2 == 0:
    #     k = 3
    # elif ran2 == 1:
    #     k = 5
    # elif ran2 == 2:
    #     k = 7
    # if rand2 > 3:
    #     if rand1 > 3:
    #         out2 = gasuss_blur(out, k, ran3)
    #     else:
    #         out2 = gasuss_blur(image1, k, ran3)
    # # if rand1 > 3:
    # #     if rand2 > 3:
    # #         return yellowing(out2)
    # #     else:
    # #         return yellowing(out)
    # # else:
    # #     return yellowing(image1)
    #
    # if rand2 <= 3:
    #     if rand1 > 3:
    #         return out
    #     else:
    #         return image1
    # else:
    #     return out2
    # # return yellowing(image1)

    # 只做高斯模糊90%
    ran2 = random.randint(0, 2)
    ran3 = random.randint(1, 5)
    rand1 = random.randint(1, 10)
    if ran2 == 0:
        k = 3
    elif ran2 == 1:
        k = 5
    elif ran2 == 2:
        k = 7
    # if rand1 > 1:
    #     out2 = gasuss_blur(image1, k, ran3)
    #     return out2
    out2 = gasuss_blur(image1, 3, 1)
    return out2
    #return yellowing(image1)


def processImage(filesoure, destsoure, name):
    """
     filesoure是存放待转换图片的目录
     destsoure是存在输出转换后图片的目录
     name是文件名
     imgtype是文件类型
     """
    # 打开图片
    # im = Image.open(filesoure + name)
    print(name)
    im = cv2.imread(filesoure + name)
    im2 = operation(im)
    cv2.imwrite(destsoure + name, im2)


def run():
    # 切换到源目录，遍历源目录下所有图片
    os.chdir(MyPath)
    for i in os.listdir(os.getcwd()):
        # 检查后缀
        # postfix = os.path.splitext(i)[1]
        # if postfix == '.jpg' or postfix == '.png':
        processImage(MyPath, OutPath, i)
        #print("--------------" + i + "----------------")


if __name__ == '__main__':
    run()
