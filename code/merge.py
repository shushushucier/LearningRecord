import cv2
import os

# 源目录
MaskPath = 'E:\\learning\\dachuang\\cyclegan\\program\\detectron2-master\\outputs2\\'
# 输出目录1
ImgPath1 = 'E:\\learning\\dachuang\\cyclegan\\program\\CycleganTest\\results\\pix2cor(l100)\\test_latest\\images2\\'
ImgPath2 = 'E:\\learning\\dachuang\\cyclegan\\program\\CycleganTest\\results\\pix1cor(l100)\\test_latest\\images2\\'

OutPath = 'E:\\learning\\dachuang\\cyclegan\\program\\CycleganTest\\results\\resCor\\'

if __name__ == '__main__':
    dirMask = os.listdir(MaskPath)
    num = 1
    for im in dirMask:
        fileName = os.path.splitext(im)[0]
        mask = os.path.join(MaskPath, im)
        img1 = os.path.join(ImgPath1, fileName+'.png')
        img2 = os.path.join(ImgPath2, fileName+'.png')
        out = os.path.join(OutPath, fileName+'.png')
        img11 = cv2.imread(img1)
        img22 = cv2.imread(img2)
        # print(im)
        # print(img22)
        # cv2.imshow("aa", img22)
        mask2 = cv2.imread(mask)
        imgTemp = img11

        for i in range(256):
            for j in range(256):
                # print(mask2[i][j])
                if mask2[i][j][0] <= 127 & mask2[i][j][1] <= 127 & mask2[i][j][2] <= 127:
                    imgTemp[i][j][0] = img22[i][j][0]
                    imgTemp[i][j][1] = img22[i][j][1]
                    imgTemp[i][j][2] = img22[i][j][2]
                else:
                    imgTemp[i][j][0] = img11[i][j][0]
                    imgTemp[i][j][1] = img11[i][j][1]
                    imgTemp[i][j][2] = img11[i][j][2]
                    # print("error")
        cv2.imwrite(out, imgTemp)
        num = num + 1
        print("---------------"+str(num)+"---------------------")

