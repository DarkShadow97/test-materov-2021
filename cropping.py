import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="shape.png", help = "path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("image", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Thresh", thresh)
#cnts = cv2.findCountours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
