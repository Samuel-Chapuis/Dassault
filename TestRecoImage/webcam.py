#################################################
# 												
# 		Author: Chapuis Samuel					
# 		For: Dassault Contest					
#												
################################################# 

import cv2 as cv
import rescale as rescale

import faceDetection as faceDetection


vid = cv.VideoCapture(0)

while True:
	success, frame = vid.read()                                         # Read frame by frame	
	frame = rescale.rescaleFrame(frame, scale=1.2)                      # Rescale frame

	detect_faces = faceDetection.detect_faces(frame)                    # Detect faces in the frame
	for (x, y, w, h) in detect_faces:                                   # Draw rectangles around faces
		cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)



	cv.imshow('frame', frame)                                           # Display frame
	if cv.waitKey(1) & 0xFF == 27:                                      # Wait for 'esc' to quit
		print("Quiting...")
		break

vid.release()
cv.destroyAllWindows()