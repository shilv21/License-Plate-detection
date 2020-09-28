# License Plate detection
 This project aims at developing methodology able to detect license plate and extract information at high speed processing.
# Introduction
Several traffic-related applications , such as detection of stolen vehicles, toll control and parking lot access validation involve indentification, whichh is performed 	by Automatic Licencse Plate Recognition (ALPR) systems. Therefore , in this work, we propose a complete ALPR system which could meet some requirement for deploying a ALPR system.

# How it work
![alt text](https://github.com/shilv21/License-Plate-detection/blob/master/Process.png)

**Model**:  In order to deploy the project to an mobile device, WPOD-NET model is the best choice which should be small enough yet still maintains its effectiveness. The WPOD-NET was developed using insights from YOLO, SSD and Spatial Transformer Networks (STN).

**Network Architecture**: The proposed architecture has a total of 21 convolutional layers, where 14 are inside residual blocks [8]. The size of all convolutional filters is fixed in 3 × 3. ReLU activations are used throughout the entire network, except in the detection block. There are 4 max pooling layers of size 2 × 2 and stride 2 that reduces the input dimensionality by a factor of 16. Finally, the detection block has two parallel convolutional layers.

![Detailed WPOD-NET architecture.](https://www.researchgate.net/profile/Claudio_Jung/publication/327861610/figure/fig3/AS:684600871366658@1540232975469/Detailed-WPOD-NET-architecture.png)

**OCR**: Tesseract could handle this task well. So we did not train a new model for this task.

**Model for mobile** : We use a pretrained model-Yolov2 tiny to deploy on Android. This model was trained with the same dataset in WPOD-NET training.

**DataSet**: 
Collectiing license plates on Google, especially license plates in country that you are concerned about. 
Making label by LabelImg.
Making a data of background images.
Making a large dataset by combine each license plate with all background images.
Increasing the dataset by Image augmentation.

# Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisites
Make sure you have python 3 and Anaconda installed on your environment.
It is better to deploy model in GCP VM-instance for higher processing.
## Project Structure
There are 3 main part of the project. They are AppDetectLicense, android-yolo-v2 and core python scripts.

 ### Core Python scripts:
**lib_detection.py** is the heart of project. It prepares image preprocessing function, license plate segmentation function and also function for calling the model.
In detection.py, we bring the **lib_detection.py** to practice. This python script will return an image of license segmentation with standard format for two type of
license plates which are common is Korea. Usage: **python dectection.py** 
With image segmentation, it will be the input for **pytesseract.py** which return a result of characters and digits on a plate.
Moreover, we build some python scripts  for synthesizing purpose when deploying an application for end users.

### AppDetectLicense:
This application is actualization bunch of theses above. This step was facing to some challenges. Some of them are processing speed, quality of images or videos,
etc…,
To solve the problem, we split application into 2 parts which make application run smoothly.
Usage: Running file **detect.exe** before running file **showvideo.exe** for importing your video or turning on camera.

### Android-yolo-v2:
For purpose of deploying on mobile, we need to change the model because of low computation of mobile devices. Therefore, YOLO is the most potential candidate which match up all requirement of the project.
Especially, **Yolo-v2-tiny** is properly available on most of mobile devices.
For usage of this part, you’ll  need android studio set up on your computer to deploy on your device when connection is done between these two devices.
# Output samples:
 ![alt text](https://github.com/shilv21/License-Plate-detection/blob/master/image1.png)
 ![alt text](https://github.com/shilv21/License-Plate-detection/blob/master/image2.jpeg)

# For more samples, please visit the demo.mp4.
