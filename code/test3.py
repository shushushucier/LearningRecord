import numpy as np
import cv2


def Contrast_and_Brightness(alpha, beta, img):
    blank = np.zeros(img.shape, img.dtype)
    # dst = alpha * img + beta * blank
    dst = cv2.addWeighted(img, alpha, blank, 1-alpha, beta)
    return dst


if __name__ == '__main__':
    img = cv2.imread("E:\\learning\\programming\\machineLearning\\dataset\\cyclegan\\B\\3146.jpg")
    img2 = img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # img2 = Contrast_and_Brightness(1, -50, img2)
    cv2.imshow("aa", img2)
    cv2.waitKey(0)