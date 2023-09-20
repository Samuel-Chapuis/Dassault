import cv2 as cv
import rescale as rescale

vid = cv.VideoCapture(0)


while True:
	ret, frame = vid.read()	
	#frame = rescale.rescaleFrame(frame, scale=1.3)
	cv.imshow('frame', frame)
	if cv.waitKey(1) & 0xFF == ord('q'):
		break

vid.release()
cv.destroyAllWindows()