#!/usr/bin/python 2

import cv2
import sys
import math
import time
import os

# Set up cascade
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

# Get video
video_capture = cv2.VideoCapture(0)

# Set some colours
black = (0, 0, 0)
blue = (255, 0, 0)
green = (0, 255, 0)
red = (0, 0, 255)

# Sets a starting point for the face location
fpoint = [0, 0]

# Run it for a set time
starttime = time.time()
duration = 30
while True:
    if time.time() - starttime < duration:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # Convert to greyscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect the faces
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=1,
            minSize=(80, 80),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )

        if len(faces) > 0:
            smallest_dist = 10**10
            closest_face = "none"
            for (x, y, w, h) in faces:
                distance = abs(math.sqrt((fpoint[0]+x)*2 + ((fpoint[1]+y)*2)))
                if distance < smallest_dist:
                    smallest_dist = distance
                    closest_face = [x, y, w, h]

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), black, 4)
            cfacelist = [closest_face]
            if closest_face != "none":
                for (x, y, w, h) in cfacelist:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), red, 2)
                    fpoint = [x, y]

        # Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        for (x, y, w, h) in cfacelist:
            cv2.imwrite("winner.png", frame[y: y + h, x: x + w])
        i = 0
        for (w, y, w, h) in faces:
            cv2.imwrite("loser" + str(i) + ".png", frame[y: y + h, x: x + w])
            i += 1
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

os.system('winner.png')
'''image = cv2.imread("winner.png", CV_LOAD_IMAGE_COLOR)
#cv2.namedWindow("Display winner window", WINDOW_NORMAL)
cv2.imshow("Winner", image)'''
