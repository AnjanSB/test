import argparse
import imutils
import cv2
path ="white dot.png"
  
# reading the image in grayscale mode
gray = cv2.imread(path, 0)
  
# threshold
th, threshed = cv2.threshold(gray, 100, 255, 
          cv2.THRESH_BINARY|cv2.THRESH_OTSU)
  
# findcontours
cnts = cv2.findContours(threshed, cv2.RETR_LIST, 
                    cv2.CHAIN_APPROX_SIMPLE)[-2]

xcnts = []
  
for c in cnts:
    if 3<cv2.contourArea(c) :
       	M = cv2.moments(c)
        cX = int(M["m10"] / M["m00"])
	    cY = int(M["m01"] / M["m00"]) 
    xcnts.append([cX,cY,2*cX,2*cY])

print(xcnts)