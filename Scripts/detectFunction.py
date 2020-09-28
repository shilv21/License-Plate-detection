
import cv2
from lib_detection import load_model, detect_lp, im2single
from matplotlib import pyplot
import sys
import os
import pytesseract
from PIL import Image, ImageDraw
import numpy as np

def detectvideo(img, total):
# Load model LP detection
    wpod_net_path = "model/wpod-net_update1.json"
    wpod_net = load_model(wpod_net_path)
    # config = ('-l kor --oem 1 --psm 3')

    img = cv2.resize(img, (500, 500))  

    # Max and min size of one dimension in the picture
    Dmax = 608
    Dmin = 500

    # Lấy tỷ lệ giữa W và H của ảnh và tìm ra chiều nhỏ nhất
    ratio = float(max(img.shape[:2])) / min(img.shape[:2])
    side = int(ratio * Dmin)
    bound_dim = min(side, Dmax)

    _ , LpImg, lp_type = detect_lp(wpod_net, im2single(img), bound_dim, lp_threshold=0.5)


    if (len(LpImg)):

    # Processing and reading the license plate
        # imgL= cv2.cvtColor(LpImg[0],cv2.COLOR_RGB2BGR )
        link= str(total)+'.jpg'
        pyplot.imsave(os.path.join('LicensePlate',link),LpImg[0])
    
    

        # Segmenting the character from license plate
        pytesseract.pytesseract.tesseract_cmd = "D:/Tesseract-OCR/tesseract.exe"


        # config = ('-l eng --oem 1 --psm 3')
        config = ('--tessdata-dir "LicensePlate" -l kor --oem 3 --psm 4')

        # # Print recognized text
        # print(text)
        # Grayscale image
        img1 = Image.open(os.path.join('LicensePlate',link)).convert('L') 
        ret,img1 = cv2.threshold(np.array(img1), 125, 255, cv2.THRESH_BINARY) 
        # Older versions of pytesseract need a pillow image
        # Convert back if needed
        img1 = Image.fromarray(img1.astype(np.uint8))

        text= pytesseract.image_to_string(img1, lang="kor", config=config)
    return text if (len(LpImg)) else "????"