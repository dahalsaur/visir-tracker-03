import cv2
import sys
import time
import numpy as np
from CameraController import CameraController
from Marker import CMarker
from Face import Face

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

vPoints = []

def collectVPoints(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        vPoints.append([x, y])
        
        
cv2.namedWindow('Camera')
cv2.setMouseCallback('Camera',collectVPoints)

controller = CameraController(16)
controller.start()
time.sleep(1)
frame_counter = 0
attenuation = 0.5
while True:
    frame = controller.getFrame()
    frame_counter += 1
    faces = faceCascade.detectMultiScale(frame)
    CMarker.markFaces(frame, faces)
    
    #if (frame_counter % 10 == 0):
    #    print("10th frame")
    #    corners = cv2.goodFeaturesToTrack(frame,50,0.01,10)
        
    #Marker.markPoints(mask, corners)
    
    
    #cv2.add(frame, mask)
    cv2.imshow('Camera', frame)
    key = cv2.waitKey(5)
    if key == 27 or key == 'q':
        break
controller.stop()