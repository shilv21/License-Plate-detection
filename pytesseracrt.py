#USAGE: CHECKING THE CHARACTER OF EACH IMAGE IN THE LicensePlate FOLDER
import cv2
import sys
import pytesseract
from PIL import Image, ImageDraw
import numpy as np
import os
if __name__ == '__main__':
 
  # Uncomment the line below to provide path to tesseract manually
  # pytesseract.pytesseract.tesseract_cmd = "D:/Tesseract-OCR/tesseract.exe"
 
  # Define config parameters.
  # '-l eng'  for using the English language
  # '--oem 1' for using LSTM OCR Engine
  config = ('-l eng --oem 1 --psm 3')
  # config = ('--tessdata-dir "data" -l kor --oem 2 --psm 4')
  # Read image from disk
  file= open('LicensePlate/license.txt',"w")
  for imPath in os.listdir('LicensePlate'):
    
  # # Print recognized text
  # print(text)
  # Grayscale image
    img = Image.open(os.path.join('LicensePlate',imPath)).convert('L')
    ret,img = cv2.threshold(np.array(img), 125, 255, cv2.THRESH_BINARY)

    # Older versions of pytesseract need a pillow image
    # Convert back if needed
    img = Image.fromarray(img.astype(np.uint8))

    text= pytesseract.image_to_string(img, lang="kor")
    print(text)
    file.write(text)

