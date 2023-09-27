# Function: Detect faces in a frame
# Input: frame
# Output: frame with rectangles around faces

# Author: Chapuis Samuel

import	cv2	as	cv

face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_faces(frame):
    # Convert the frame to grayscale for face detection
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return frame
