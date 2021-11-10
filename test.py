import numpy as np
import argparse
import imutils
import cv2
import keyboard
import time

videoCaptureObject = cv2.VideoCapture(0)
#if we want cam on
result = True
snapshots = ["front.jpg", "back.jpg", "top.jpg", "left.jpg", "right.jpg"]
i = 0;
#for name in snapshots:s
while(result):
    ret,frame = videoCaptureObject.read()
    cv2.imshow("Capturing Video",frame)
    #if keyboard.is_pressed("q"):
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        videoCaptureObject.release()
        cv2.destroyAllWindows()
    if keyboard.is_pressed('s'):
        if i < len(snapshots):
            cv2.imwrite(snapshots[i],frame)
            cv2.imshow(snapshots[i], frame)
            i += 1
            time.sleep(1)
        else:
            result=False
