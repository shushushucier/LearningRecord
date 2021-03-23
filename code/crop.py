import os
import cv2

# 源目录
MyPath = 'E:\\learning\\dachuang\\cyclegan\\carDS\\car\\'
# 输出目录
OutPath = 'E:\\learning\\dachuang\\cyclegan\\carDS\\carCrop\\'


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
    print(name)
    print(im)
    sp = im.shape
    sz1 = sp[0]
    sz2 = sp[1]
    if sz1 >= 256:
        if sz2 >= 256:
            a = int(sz1 / 2 - 128)  # x start
            b = int(sz1 / 2 + 128)  # x end
            c = int(sz2 / 2 - 128)  # y start
            d = int(sz2 / 2 + 128)  # y end
            im2 = im[a:b, c:d]
            cv2.imwrite(destsoure + name, im2)


def run():
    # 切换到源目录，遍历源目录下所有图片
    print(MyPath)
    os.chdir(MyPath)
    for i in os.listdir(os.getcwd()):
        # 检查后缀
        # postfix = os.path.splitext(i)[1]
        # if postfix == '.jpg' or postfix == '.png':
        print(i)
        processImage(MyPath, OutPath, i)
        print("--------------" + i + "----------------")


if __name__ == '__main__':
    run()
