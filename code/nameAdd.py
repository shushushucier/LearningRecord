# -*- coding:utf8 -*-

import os
import re
'''
添加后缀
'''

class BatchRename():
    '''
    批量重命名文件夹中的图片文件
    '''

    def __init__(self):
        # 我的图片文件夹路径horse
        self.path = 'E:\\learning\\dachuang\\cyclegan\\carDS\\已完成\\yin\\carscratch\\'

    # def num(self, nam):
    #     name = re.sub("\D", "", nam)
    #     return name

    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)

        i = 1
        for item in filelist:

            src = os.path.join(os.path.abspath(self.path), item)
            prefix = item.split(".")[0]
            nameNew = prefix+"_yin"
            print(nameNew)
            # temp = self.num(item)
            dst = os.path.join(os.path.abspath(self.path), nameNew + '.jpg')
            # dst = os.path.join(os.path.abspath(self.path), temp + '.jpg')
            try:
                os.rename(src, dst)
                print('converting %s to %s ...' % (src, dst))
                i = i + 1

            except:
                continue
        print('total %d to rename & converted %d jpgs' % (total_num, i))


if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()
