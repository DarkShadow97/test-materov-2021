import numpy as np
import argparse
import imutils
import cv2
import keyboard
import time

i = 0

center = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\center.png")
top = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\top.png")
bottom = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\bottom.png")
left = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\left.png")
right = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\right.png")
blank = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\blank.png")

centerResize = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\blank.png")
cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\centerResize.png", blank)
topResize = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\blank.png")
cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\topResize.png", topResize)
bottomResize = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\blank.png")
cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\bottomResize.png", bottomResize)
leftResize = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\blank.png")
cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\leftResize.png", leftResize)
rightResize = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\blank.png")
cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\rightResize.png", rightResize)
blankTopResize = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\blank.png")
cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\blankTopResize.png", blankTopResize)
blankBottomResize = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\blank.png")
cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\blankBottomResize.png", blankBottomResize)

imagesresized = ["C:\\Users\\alexa\\Desktop\\photomosaic\\centerResize.png",
    "C:\\Users\\alexa\\Desktop\\photomosaic\\topResize.png",
    "C:\\Users\\alexa\\Desktop\\photomosaic\\bottomResize.png",
    "C:\\Users\\alexa\\Desktop\\photomosaic\\leftResize.png",
    "C:\\Users\\alexa\\Desktop\\photomosaic\\rightResize.png",
    "C:\\Users\\alexa\\Desktop\\photomosaic\\blankResize.png"
]

snapshots = ["C:\\Users\\alexa\\Desktop\\photomosaic\\center.png",
    "C:\\Users\\alexa\\Desktop\\photomosaic\\top.png",
    "C:\\Users\\alexa\\Desktop\\photomosaic\\bottom.png",
    "C:\\Users\\alexa\\Desktop\\photomosaic\\left.png",
    "C:\\Users\\alexa\\Desktop\\photomosaic\\right.png"]

resizeimage = [
    centerResize,
    topResize,
    bottomResize,
    leftResize,
    rightResize]

def resize_image(img, scale_w, scale_h):
    return cv2.resize(img, (int(img.shape[1]*scale_w), int(img.shape[0]*scale_h)))

#---------crop and resize the image to a height of 250 pixels-----------
def cropping(image):
    image = cv2.imread(image)
    cv2.imshow("Image", image)
    cv2.waitKey(0)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 100, 300, cv2.THRESH_BINARY_INV)[1]
    cv2.imshow("Thresh", thresh)
    cv2.waitKey(0)

    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    c = max(cnts, key=cv2.contourArea)

    output = image.copy()
    cv2.drawContours(output, [c], -1, (0, 255, 0), 3)
    (x, y, w, h) = cv2.boundingRect(c)
    text = "original, num_pts = {}".format(len(c))
    cv2.putText(output, text, (x,y - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)



    #Crop the image based on the points of the bounding box, show the cropped image
    cropped = image[y:y+h, x:x+w]
    file = snapshots[i]
    cv2.imwrite(file, cropped)
    #cv2.imshow("Cropped Image", cropped)
    #cv2.waitKey(0)

def photomosaic():
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    i = 1
    while result:
        ret, frame = videoCaptureObject.read()
        cv2.imshow("Capturing Video", frame)
        # deletes every frame as the next one comes on, closes all windows when q is pressed
        if cv2.waitKey(1) == ord('q'):
            videoCaptureObject.release()
            cv2.destroyAllWindows()
        cropping(snapshots[0])
        center_height = snapshots[0].shape[0]
        center_width = snapshots[0].shape[1]
        # when s is pressed
        if keyboard.is_pressed('s'):
            # and the index is less than the length of the snapshot list
            if i < len(snapshots):
                # take as snapshot, save it, show it
                cv2.imwrite(snapshots[i], frame)
                cv2.imshow(snapshots[i], frame)
                cropping(snapshots[i])
                resize_image(snapshots[i], )
                resizeimage[i] = cv2.imread(imagesresized[i])
                time.sleep(1)
                i += 1
            else:
                result = False



        #---------rereading the original images from the snapshots-----------
        center = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\center.png")
        top = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\top.png")
        bottom = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\bottom.png")
        left = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\left.png")
        right = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\right.png")
        blank = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\blank.png")

        j = 1
        if j < len(snapshots):
            width_ratio = center_width/snapshots[j].shape[0]
            height_ratio = center_height/snapshots[j].shape[1]
            if j < 3:
                resize_image(snapshots[j], width_ratio, 1)
                j += 1
            else:
                resize_image(snapshots[j], 1, height_ratio)
                j += 1
