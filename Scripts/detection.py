#USAGE: FOR DETECT LICENSE FROM A PICTURE
import cv2
from lib_detection import load_model, detect_lp, im2single
from matplotlib import pyplot
import sys
import os
# Đường dẫn ảnh, các bạn đổi tên file tại đây để thử nhé
# img_path = "test/40.jpg"
if len(sys.argv) < 2:
    print('Usage: python ocr_simple.py image.jpg')
    sys.exit(1)
imgLink= sys.argv[1]
img_path= os.path.join('videos', imgLink)
# Load model LP detection
wpod_net_path = "model/wpod-net_update1.json"
wpod_net = load_model(wpod_net_path)

# Read image as input
Ivehicle = cv2.imread(img_path)


# Max and min size of one picture's dimension
Dmax = 608
Dmin = 288

# Calcutlating the W/H and find the min dimension
ratio = float(max(Ivehicle.shape[:2])) / min(Ivehicle.shape[:2])
side = int(ratio * Dmin)
bound_dim = min(side, Dmax)

_ , LpImg, lp_type = detect_lp(wpod_net, im2single(Ivehicle), bound_dim, lp_threshold=0.5)


if (len(LpImg)):

    # Processing and reading the license plate
    imgL= cv2.cvtColor(LpImg[0],cv2.COLOR_RGB2BGR )
    pyplot.imsave(os.path.join('videos',imgLink),imgL)
    # cv2.imwrite('./videos/1.jpg',imgL)
    cv2.imshow("Bien so", imgL)
    
    
    cv2.waitKey()

cv2.destroyAllWindows()