import cv2
import numpy as np
import math
import os

# fake
FakePath = 'E:\\learning\\dachuang\\cyclegan\\program\\CycleganTest\\results\\pix2bw(la200)\\test_latest\\images2\\'
# real
RealPath = 'E:\\learning\\dachuang\\cyclegan\\program\\CycleganTest\\results\\pix2bw(la200)\\test_latest\\images3\\'


## 无参考情况下的图像清晰度评估方法
def brenner(img):
    '''
    :param img: 2D grey Image
    :return:    a float number that indicates the sharpness of the image
    '''
    # height, width = len(img), len(img[0])
    height, width = np.shape(img)
    sharpness = 0.0
    for x in range(0, height - 2):
        for y in range(0, width):
            sharpness += (int(img[x][y]) - int(img[x + 2][y])) ** 2
    return sharpness


def Laplacian(img):
    '''
    :param img: 2D grey Image
    :return:    a float number that indicates the sharpness of the image
    '''
    height, width = np.shape(img)
    assert height == 256 and width == 256
    return cv2.Laplacian(img, cv2.CV_64F).var()


def SMD(img):
    '''
    :param img: narray 2D grey image
    :return: float 图像越清晰越大
    '''
    shape = np.shape(img)
    sharpness = 0.0
    for x in range(1, shape[0] - 1):
        for y in range(0, shape[1]):
            sharpness += math.fabs(int(img[x, y]) - int(img[x, y - 1]))
            sharpness += math.fabs(int(img[x, y]) - int(img[x + 1, y]))
    return sharpness


def SMD2(img):
    '''
    :param img:
    :return:
    '''
    shape = np.shape(img)
    sharpness = 0.0
    for x in range(0, shape[0] - 1):
        for y in range(0, shape[1] - 1):
            sharpness += math.fabs(int(img[x, y]) - int(img[x + 1, y])) * math.fabs(int(img[x, y]) - int(img[x, y + 1]))
    return sharpness


def Vollath(img):
    '''
    :param img:narray 2D gery image
    :return: float number
    '''
    shape = np.shape(img)
    u = np.mean(img)
    sharpness = -shape[0] * shape[1] * (u ** 2)
    for x in range(0, shape[0] - 1):
        for y in range(0, shape[1]):
            sharpness += int(img[x, y]) * int(img[x + 1, y])
    return sharpness


## 有参考图像情况下的清晰度// (其实这个不光是清晰度了) 就是比较两个图像的差异
def Divergence(fake_img, real_img):
    '''
    :param fake_img: 生成图片
    :param real_img: 真实图片
    :return:   返回两张图片的散度损失
    '''
    assert fake_img.shape[0] == real_img.shape[0] and fake_img.shape[1] == real_img.shape[1]
    D_AB = 0.0
    height, width, channel = fake_img.shape[0], fake_img.shape[1], fake_img.shape[2]
    for i in range(height):
        for j in range(width):
            for k in range(channel):
                D_AB += fake_img[i][j][k] * np.log(fake_img[i][j][k] / real_img[i][j][k]) - fake_img[i][j][k] + \
                        real_img[i][j][k]

    return D_AB


def showImage(filepath, i: int):
    '''
    :param filepath: 存放生成图片和真实图片的路径
    :param i: 第i张图片
    :return:  展示两张图片
    '''
    fake_img = cv2.imread(filepath + str(i) + ".png")
    real_img = cv2.imread(filepath + str(i) + ".png")
    height, width, channel = fake_img.shape[0], fake_img.shape[1], fake_img.shape[2]
    print(height, width, channel)
    concat_img = np.zeros((height, width * 2, channel), np.uint8)
    concat_img[0:height, 0:width, :] = fake_img[0:height, 0:width, :]
    concat_img[0:height, width:, :] = real_img[0:height, 0:width, :]
    cv2.imshow("", concat_img)
    cv2.waitKey(0)


def evaluate(fake, real):
    loss = 0.0

    fake_sharpness = []
    real_sharpness = []

    brennerFake = brenner(fake)
    brennerReal = brenner(real)

    laplacianFake = Laplacian(fake)
    laplacianReal = Laplacian(real)

    SMDFake = SMD(fake)
    SMDReal = SMD(real)

    SMD2Real = SMD2(real)
    SMD2Fake = SMD2(fake)

    VollathFake = Vollath(fake)
    VollathReal = Vollath(real)

    fake_sharpness.append(brennerFake)
    real_sharpness.append(brennerReal)

    fake_sharpness.append(laplacianFake)
    real_sharpness.append(laplacianReal)

    fake_sharpness.append(SMDFake)
    real_sharpness.append(SMDReal)

    fake_sharpness.append(SMD2Fake)
    real_sharpness.append(SMD2Real)

    fake_sharpness.append(VollathFake)
    real_sharpness.append(VollathReal)

    loss = sum(abs(np.array(fake_sharpness) - np.array(real_sharpness)))

    # loss += Divergence(fake, real)

    return brennerFake, brennerReal, laplacianFake, laplacianReal, SMDFake, SMDReal, SMD2Fake, SMD2Real, VollathFake, VollathReal


if __name__ == '__main__':
    fakeBrenner = []
    realBrenner = []
    fakeLaplacian = []
    realLaplacian = []
    fakeSMD = []
    realSMD = []
    fakeSMD2 = []
    realSMD2 = []
    fakeVollath = []
    realVollath = []

    print(RealPath)
    fakeNames = os.listdir(FakePath)
    num = len(fakeNames)
    # loss = 0.0
    for im in fakeNames:
        imgReal = os.path.join(RealPath, im)
        imgFake = os.path.join(FakePath, im)
        imgReal2 = cv2.imread(imgReal)
        imgFake2 = cv2.imread(imgFake)
        imgRealGray = cv2.cvtColor(imgReal2, cv2.COLOR_BGR2GRAY)
        imgFakeGray = cv2.cvtColor(imgFake2, cv2.COLOR_BGR2GRAY)
        brennerFake, brennerReal, laplacianFake, laplacianReal, SMDFake, SMDReal, SMD2Fake, SMD2Real, VollathFake, VollathReal = evaluate(imgFakeGray, imgRealGray)
        fakeBrenner.append(brennerFake)
        realBrenner.append(brennerReal)
        fakeLaplacian.append(laplacianFake)
        realLaplacian.append(laplacianReal)
        fakeSMD.append(SMDFake)
        realSMD.append(SMDReal)
        fakeSMD2.append(SMD2Fake)
        realSMD2.append(SMD2Real)
        fakeVollath.append(VollathFake)
        realVollath.append(VollathReal)

        print(im + "    " + "brennerFake："+str(brennerFake)+"     "+"brennerReal："+str(brennerReal))
        print(im + "    " + "laplacianFake："+str(laplacianFake)+"     "+"laplacianReal："+str(laplacianReal))
        print(im + "    " + "SMDFake：" + str(SMDFake) + "     " + "SMDReal：" + str(SMDReal))
        print(im + "    " + "SMD2Fake：" + str(SMD2Fake) + "     " + "SMD2Real：" + str(SMD2Real))
        print(im + "    " + "VollathFake：" + str(VollathFake) + "     " + "VollathReal：" + str(VollathReal))
    print("brennerReal"+"     "+str(sum(realBrenner)/num))
    print("brennerFake"+"     "+str(sum(fakeBrenner)/num))
    print("laplacianReal" + "     " + str(sum(realLaplacian)/num))
    print("laplacianFake" + "     " + str(sum(fakeLaplacian)/num))
    print("SMDReal" + "     " + str(sum(realSMD)/num))
    print("SMDFake" + "     " + str(sum(fakeSMD)/num))
    print("SMD2Real" + "     " + str(sum(realSMD2)/num))
    print("SMD2Fake" + "     " + str(sum(fakeSMD2)/num))
    print("VollathReal" + "     " + str(sum(realVollath)/num))
    print("VollathFake" + "     " + str(sum(fakeVollath)/num))
