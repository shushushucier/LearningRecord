import cv2
import os

# 源目录
MaskPath = 'E:\\learning\\dachuang\\cyclegan\\program\\detectron2-master\\outputs2\\'
# 输出目录
ImgPath = 'E:\\learning\\programming\\machineLearning\\dataset\\cyclegan\\pix_black\\B\\test\\'

OutPath = 'E:\\learning\\programming\\machineLearning\\dataset\\cyclegan\\pix_black\\maskB1\\test\\'

if __name__ == '__main__':
    dirMask = os.listdir(MaskPath)
    num = 1
    for im in dirMask:
        mask = os.path.join(MaskPath, im)
        img = os.path.join(ImgPath, im)
        out = os.path.join(OutPath, im)
        img2 = cv2.imread(img)
        mask2 = cv2.imread(mask)
        imgTemp = img2

        for i in range(256):
            for j in range(256):
                # print(mask2[i][j])
                if mask2[i][j][0] <= 127 & mask2[i][j][1] <= 127 & mask2[i][j][2] <= 127:
                    imgTemp[i][j][0] = 0
                    imgTemp[i][j][1] = 0
                    imgTemp[i][j][2] = 0
                else:
                    pass
                    # print("error")
        cv2.imwrite(out, imgTemp)
        num = num + 1
        print("---------------"+str(num)+"---------------------")

