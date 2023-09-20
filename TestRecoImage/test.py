import cv2 as cv

# Load the pre-trained face detection classifier
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

vid = cv.VideoCapture(0)

while True:
    ret, frame = vid.read()
    
    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Iterate over the detected faces
    for (x, y, w, h) in faces:
        # Draw a rectangle around the detected face
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Square the detected face
        if w > h:
            diff = (w - h) // 2
            y = y - diff
            h = w  # Make the height equal to width
        else:
            diff = (h - w) // 2
            x = x - diff
            w = h  # Make the width equal to height

        squared_face = frame[y:y + h, x:x + w]
        cv.imshow('Squared Face', squared_face)

    cv.imshow('frame', frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv.destroyAllWindows()