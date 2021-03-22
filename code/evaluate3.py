import os
import cv2
import numpy as np
from skimage.measure import compare_psnr
from skimage.metrics import structural_similarity as ssim

# fake
FakePath = 'E:\\learning\\dachuang\\cyclegan\\program\\CycleganTest\\results\\pixCaryin1(la100)\\test_latest\\imageRealA\\'
# real
RealPath = 'E:\\learning\\dachuang\\cyclegan\\program\\CycleganTest\\results\\pixCaryin1(la100)\\test_latest\\imageRealB\\'

if __name__ == '__main__':
    loss = []
    fakeNames = os.listdir(FakePath)
    num = len(fakeNames)
    for im in fakeNames:
        lossT = 0
        imgReal = os.path.join(RealPath, im)
        imgFake = os.path.join(FakePath, im)
        imgReal2 = cv2.imread(imgReal)
        imgFake2 = cv2.imread(imgFake)
        imgRealGray = cv2.cvtColor(imgReal2, cv2.COLOR_BGR2GRAY)
        imgFakeGray = cv2.cvtColor(imgFake2, cv2.COLOR_BGR2GRAY)
        imgRealGray2 = np.array(imgRealGray)
        imgFakeGray2 = np.array(imgFakeGray)
        for i in range(256):
            for j in range(256):
                lossT = lossT + abs(imgFakeGray2[i][j]-imgRealGray2[i][j])
        loss.append(lossT)
        print(im+"\tloss:\t"+str(lossT))
    print(str(sum(loss)/num))