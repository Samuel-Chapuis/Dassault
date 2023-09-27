#################################################
# 												
# 		Author: Chapuis Samuel					
# 		For: Dassault Contest					
#												
################################################# 

import cv2 as cv
import rescale as rescale

vid = cv.VideoCapture(0)


while True:
	success, frame = vid.read()									# Read frame by frame	
	frame = rescale.rescaleFrame(frame, scale=1.2)				# Rescale frame





	cv.imshow('frame', frame)									# Display frame
	if cv.waitKey(1) & 0xFF == 27:								# Wait for 'esc' to quit
		print("Quiting...")
		break

vid.release()
cv.destroyAllWindows()