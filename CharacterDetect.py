# Project - 20 Marks
# ID - 181-115-027
# Name - Rahat Hasan Chowdhury
# Batch 44(A)


#opencv-python library fuction
#read,write the code
import cv2

#Python-tesseract is an optical
# character recognition (OCR) tool for python.
# That is, it will recognize and “read” the text embedded in images.

import pytesseract

# I had to add this tool in order to making Pytesseract Work

pytesseract.pytesseract.tesseract_cmd = 'E:\\Autumn 3-3 2020\\AI\\Project\\AI Project\\AI Project\\Tesseract-OCR\\tesseract.exe'

#read image from stored folder/path
img = cv2.imread('test.jpg')

#Image result for what is cvtColor python
#cvtColor() method

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# print(img)


### Detecting Characters
hImg, wImg,_ = img.shape

#store image box return char boundaries
boxes = pytesseract.image_to_boxes(img)

#run a loop
# Loop will be running as long as the code detects character in the input file
for b in boxes.splitlines():
    b = b.split(' ')
    print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x, hImg-y), (w, hImg-h), (0, 0, 225), 2)
    cv2.putText(img, b[0], (x, hImg-y+25), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 225),2)


cv2.imshow('Result',img)
cv2.waitKey(0)



