# -*- coding:utf8 -*-

import os
import cv2
import re


class BatchRename():
    '''
    批量重命名文件夹中的图片文件
    '''

    def __init__(self):
        # 原图像地址
        self.sourcePath = 'E:\\learning\\dachuang\\cyclegan\\program\\CycleganTest\\results\\pixCaryin1(la100)\\test_latest\\images\\'
        # 目标图像地址
        self.desPath = 'E:\\learning\\dachuang\\cyclegan\\program\\CycleganTest\\results\\pixCaryin1(la100)\\test_latest\\imageFake\\'

    def rename(self):
        filelist = os.listdir(self.sourcePath)
        for item in filelist:
            if item.endswith('.png'):
                if "fake" in item:
                    if "B" in item:
                        item2 = "".join(re.findall("\d+", item))
                        src = os.path.join(os.path.abspath(self.sourcePath), item)
                        dst = os.path.join(os.path.abspath(self.desPath), item2 + '.png')
                        try:
                            img = cv2.imread(src)
                            cv2.imwrite(dst, img)
                            print('converting %s to %s ...' % (src, dst))
                        except:
                            continue
                # if "real" in item:
                #     if "B" in item:
                #         item2 = "".join(re.findall("\d+", item))
                #         src = os.path.join(os.path.abspath(self.sourcePath), item)
                #         dst = os.path.join(os.path.abspath(self.desPath), item2 + '.png')
                #         try:
                #             img = cv2.imread(src)
                #             cv2.imwrite(dst, img)
                #             print('converting %s to %s ...' % (src, dst))
                #         except:
                #             continue

    # def rename(self):
    #     filelist = os.listdir(self.sourcePath)
    #     for item in filelist:
    #         if item.endswith('.jpg'):
    #             item2 = "".join(re.findall("\d+", item))
    #             src = os.path.join(os.path.abspath(self.sourcePath), item)
    #             dst = os.path.join(os.path.abspath(self.desPath), item2 + '.png')
    #             try:
    #                 img = cv2.imread(src)
    #                 cv2.imwrite(dst, img)
    #                 print('converting %s to %s ...' % (src, dst))
    #             except:
    #                 continue


if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()
