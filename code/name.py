# -*- coding:utf8 -*-

import os
import re
'''
连续数字名称重命名
'''

class BatchRename():
    '''
    批量重命名文件夹中的图片文件
    '''

    def __init__(self):
        # 我的图片文件夹路径horse
        self.path = 'E:\\learning\\dachuang\\cyclegan\\carDS\\complete\\final\\finalABmohu4\\train2\\'

    # def num(self, nam):
    #     name = re.sub("\D", "", nam)
    #     return name

    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)

        i = 3475
        for item in filelist:
            if item.endswith('.jpg'):
                src = os.path.join(os.path.abspath(self.path), item)
                # temp = self.num(item)
                dst = os.path.join(os.path.abspath(self.path), str(i) + '.jpg')
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
