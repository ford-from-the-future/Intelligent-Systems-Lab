import numpy as np
import cv2 as cv
import sys
def analyze_object(img):
    img = cv.imread(img,0)
    thresh = cv.threshold(img,127,255,0)
    im2,contours,hierarchy = cv.findContours(thresh, 1, 2)
    cnt = contours[0]
    M = cv.moments(cnt)
    print(M)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    im2 = cv.cvtColor(im2, cv.COLOR_GRAY2RGB)
    cv.polylines(im2,cnt,True,(0,0,255),2)
    cv.circle(im2,(cx,cy),5,(0,0,255),1)
    cv.imshow("res",im2)
analyze_object("photo.jpg")