import numpy as np
import cv2
import os

# 调整最大值
MAX_VALUE = 100


def update(lightness, saturation):
    """
    用于修改图片的亮度和饱和度
    :param input_img_path: 图片路径
    :param output_img_path: 输出图片路径
    :param lightness: 亮度
    :param saturation: 饱和度
    """

    # 加载图片 读取彩色图像归一化且转换为浮点型
    image = cv2.imread("E:\\learning\\programming\\machineLearning\\dataset\\cyclegan\\B\\3146.jpg", cv2.IMREAD_COLOR).astype(np.float32) / 255.0

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
    cv2.imshow("test", lsImg)
    cv2.waitKey(0)
    # cv2.imwrite(output_img_path, lsImg)


if __name__ == '__main__':
    update(-10, -70)

