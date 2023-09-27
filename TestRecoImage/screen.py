#################################################
# 												
# 		Author: Chapuis Samuel					
# 		For: Dassault Contest					
#												
################################################# 

#Packages	
import cv2 as cv
import pyautogui as pyautogui
import numpy as np

import rescale as rescale
import faceDetection as faceDetection

#Mainc
while True:
	frame = cv.cvtColor(np.array(pyautogui.screenshot()), cv.COLOR_RGB2BGR)		# Take screenshot
	frame = rescale.rescaleFrame(frame, scale=0.5)								# Rescale frame
	
	frame = faceDetection.detect_faces(frame)													# Detect faces in the frame

	cv.imshow('frame', frame)													# Display frame
	if cv.waitKey(1) & 0xFF == 27:												# Wait for 'esc' to quit
		print("Quiting...")
		break

vid.release()
cv.destroyAllWindows()