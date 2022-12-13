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
    x,y,w,h = cv2.boundingRect(c)
    xcnts.append([x,y,w,h])

print(xcnts)
