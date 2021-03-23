import numpy as np
import random
import cv2


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

    ran2 = random.randint(0, 2)
    ran3 = random.randint(1, 5)
    if ran2 == 0:
        k = 3
    elif ran2 == 1:
        k = 5
    elif ran2 == 2:
        k = 7
    return out, k, ran3


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
    cv2.imshow("gasuss", out3)
    cv2.waitKey(0)
    return out3


def operation(image1):
    mean = 0
    # var = random.uniform(0.001, 0.004)
    var = 0.0001
    out, k, ran3 = gasuss_noise(image1, mean, var)
    out2 = gasuss_blur(out, k, ran3)
    return yellowing(out2)


if __name__ == '__main__':
    image = cv2.imread(
        "E:\\learning\\programming\\machineLearning\\dataset\\cyclegan\\JPEGImages\\2.jpg")
    operation(image)
