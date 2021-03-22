import os
import random


class Rename():
    def __init__(self):
        # 我的图片文件夹路径horse
        self.path = 'E:\\learning\\programming\\machineLearning\\dataset\\cyclegan\\pix_burABlack\\pix_burABlack\\train\\'

    def rename(self):
        Imgnum = 21017
        L = random.sample(range(0, Imgnum), Imgnum)
        filetype = ".jpg"  # 文件类型
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        i = 0
        for filename in filelist:
            portion = os.path.splitext(filename)  # 将文件名拆成名字和后缀
            if portion[1] == filetype:  # 检查文件的后缀
                src = os.path.join(os.path.abspath(self.path), filename)
                # temp = self.num(item)
                newname = str(L[i])
                dst = os.path.join(os.path.abspath(self.path), newname + '.jpg')
                # dst = os.path.join(os.path.abspath(self.path), temp + '.jpg')
                try:
                    os.rename(src, dst)
                    print('converting %s to %s ...' % (src, dst))
                    i = i + 1
                except:
                    continue
            print('total %d to rename & converted %d jpgs' % (total_num, i))


if __name__ == '__main__':
    demo = Rename()
    demo.rename()