import os
import cv2
from skimage.measure import compare_psnr
from skimage.metrics import structural_similarity as ssim

# fake
FakePath = 'E:\\learning\\dachuang\\cyclegan\\program\\CycleganTest\\results\\pix2bw(la25)\\test_latest\\images2\\'
# real
RealPath = 'E:\\learning\\dachuang\\cyclegan\\program\\CycleganTest\\results\\pix2bw(la25)\\test_latest\\images3\\'

if __name__ == '__main__':
    psr = []
    sim = []

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
        ss = ssim(imgRealGray, imgFakeGray)
        pp = compare_psnr(imgRealGray, imgFakeGray, data_range=255)
        sim.append(ss)
        psr.append(pp)
        print(im+"\tssim:\t"+str(ss))
        print(im+"\tpsnr:\t"+str(pp))
    print("ssim"+"     "+str(sum(sim)/num))
    print("psnr"+"     "+str(sum(psr)/num))