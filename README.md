# License Plate detection
 This project aims at developing methodoloy able to detect license plate and extract information at high speed processing.
# Introduction
	Several traffic-related applications , such as detection of stolen vehicles, toll control and parking lot access validation involve indentification, whichh is performed 	 by Automatic Licencse Plate Recognition (ALPR) systems. Therefore , in this work, we propose a complete ALPR system which could meet some requirement for deploying a 		ALPR system.
	Data preparation.
	Collectiing license plates on Google, especially license plates in Korea,
	Making a data of background images.
	Making a large dataset by combine each license plate with all background images.
	Increasing the dataset by Image augmentation.

# Training a model with WPOD_NET
# Using model for license segmentation
	Loading image file in jpg or png format.
	Calling WPOD model to filter out the license plate.
	Preprocessing image to give it a standard format in order to get high accuracy as expected.
# Optical Character Recognition.
	There are many ways to build an OCR system such as buildng a model based on deep learning, SVM or KNN algorithm.
	We choose Tesseract because of many reasons. With tesseract, we might not build own system. It make us save time preparing Korean character and digit data for training.
	Beside that, tesseract allow us to preprocess image progressively through its bullt-in parameter system.
	In practice we follow this way and get some positive outcomes.
	Furthermore, tesseract provide users API through its package which getting update usually. It helps us apply OCR easily and quickly in order to ensure the processing 		speed of application.
# Project organization
	There are 3 main part of the project. They are AppDetectLicense, android-yolo-v2 and core python scripts.

	 Core Python scripts:
		lib_detection.py is the heart of project. It prepares image preprocessing function, license plate segmentation function and also function for calling the model.
		In detection.py, we bring the lib_detection.py to practice. This python script will return an image of license segmentation with standard format for two type of
		license plates which are common is Korea. Usage: python dectection.py [Path to image]
		With image segmentation, it will be the input for pytesseract.py which return a result of characters and digits on a plate.
		Moreover, we build some python scripts  for synthesizing purpose when deploying an application for end users.

	AppDetectLicense:
		This application is actualization bunch of theses above. This step was facing to some challenges. Some of them are processing speed, quality of images or videos,
		etc…,
		To solve the problem, we split application into 2 parts which make application run smoothly.
		Usage: Running file detect.exe before running file showvideo.exe for importing your video or turning on camera.

	Android-yolo-v2:
		For purpose of deploying on mobile, we need to change the model because of low computation of mobile devices. Therefore, YOLO is the most potential candidate 
		which match up all requirement of the project.
		Especially, Yolo-v2-tiny is properly available on most of mobile devices.
		For usage of this part, you’ll  need android studio set up on your computer to deploy on your device when connection is done between these two devices.

