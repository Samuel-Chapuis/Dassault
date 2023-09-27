# Function: Detect faces in a frame
# Input: frame
# Output: frame with rectangles around faces

# Author: Chapuis Samuel

import	cv2	as	cv

face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_faces(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)                                                        # Convert the frame to grayscale for face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))      # Detect faces in the grayscale frame
    face_coordinates = [(x, y, w, h) for (x, y, w, h) in faces]                                         # Get the coordinates of the faces
    return face_coordinates
