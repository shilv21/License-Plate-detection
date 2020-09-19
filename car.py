import cv2
import numpy as np
import os
from imutils.video import FPS
import imutils
# create an overlay image. You can use any image
# foreground = np.ones((400,100,3),dtype='uint8')*255
# from reader.__main__ import main

foreground = cv2.imread(os.path.join('LicensePlate','1.jpg'))
foreground = cv2.resize(foreground,(280,200),interpolation = cv2.INTER_AREA)
# writer = cv2.VideoWriter("output.avi",cv2.VideoWriter_fourcc(*"MJPG"), 30,(640,480))
# Open the camera
cap = cv2.VideoCapture('videos/macar1.mp4')

# Set initial value of weights
alpha = 0.4
totalframes=0

while True:
    # read the background
    ret, background = cap.read()
    background = cv2.flip(background,1)
    if totalframes %1==0 and totalframes>0:
        impath= str(totalframes) + '.jpg'
        preforeground = cv2.imread(os.path.join('LicensePlate',impath))
        if preforeground is not None: foreground = preforeground
        # foreground = cv2.resize(foreground,(280,100),interpolation = cv2.INTER_AREA)
    if foreground.shape[0]==110:    
        foreground = cv2.resize(foreground,(280,200),interpolation = cv2.INTER_AREA)
    
    # Select the region in the background where we want to add the image and add the images using cv2.addWeighted()
    added_image = cv2.addWeighted(background[150:350,150:430,:],alpha,foreground[0:200,0:280,:],1-alpha,0)
    # Change the region with the result
    background[150:350,150:430] = added_image
    # For displaying current value of alpha(weights)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(background,'alpha:{}'.format(alpha),(10,30), font, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.imshow('a',background)
    k = cv2.waitKey(10)
    # Press q to break
    if k == ord('q'):
        break
    # press a to increase alpha by 0.1
    if k == ord('a'):
        alpha +=0.1
        if alpha >=1.0:
            alpha = 1.0
    # press d to decrease alpha by 0.1
    elif k== ord('d'):
        alpha -= 0.1
        if alpha <=0.0:
            alpha = 0.0
    totalframes +=1
    # writer.write(background.astype('uint8'))

# Release the camera and destroy all windows     
# writer.release()
cap.release()
cv2.destroyAllWindows()



    