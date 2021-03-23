import cv2
import numpy as np


def Contrast_and_Brightness(alpha, beta, img):
    blank = np.zeros(img.shape, img.dtype)
    # dst = alpha * img + beta * blank
    dst = cv2.addWeighted(img, alpha, blank, 1-alpha, beta)
    return dst


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
            B = int(0.1 * r + 0.56 * g + 0.3 * b)
            # G = int(0.347 * r + 0.683 * g + 0.167 * b)
            G = int(0.1 * r + 0.734 * g + 0.3 * b)
            R = int(0.1 * r + 0.734 * g + 0.18 * b)  # 约束图像像素值，防止溢出
            out3[i, j][0] = max(0, min(B, 255))
            out3[i, j][1] = max(0, min(G, 255))
            out3[i, j][2] = max(0, min(R, 255))
    # cv2.imshow("gasuss", out3)
    # cv2.waitKey(0)
    return out3


if __name__ == '__main__':
    img = cv2.imread("E:\\learning\\programming\\machineLearning\\dataset\\cyclegan\\B\\3146.jpg")
    img2 = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img2 = Contrast_and_Brightness(1, -70, img2)
    img2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2RGB)
    img2 = yellowing(img2)
    img2 = Contrast_and_Brightness(0.6, 20, img2)

    cv2.imshow("aa", img2)
    cv2.waitKey(0)