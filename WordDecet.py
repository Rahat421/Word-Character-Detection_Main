import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'E:\\Autumn 3-3 2020\\AI\\Project\\AI Project\\AI Project\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('test.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


hImg, wImg, _ = img.shape
boxes = pytesseract.image_to_data(img)

# Enumerate() iterates the value where it’s iterable and in this case the boxes.splitline() is iterable.

for x, b in enumerate(boxes.splitlines()):

    if x!=0: # Till this x = 0 (['4', '1', '1', '1', '1', '0', '116', '151', '730', '93', '-1'])
        b = b.split()
        print(b)
        if len(b)==12: # ['2', '1', '1', '0', '0', '0', '116', '151', '730', '263', '-1']
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x, y), (w+x, h+y), (0, 0, 225), 2)
            cv2.putText(img, b[11], (x+2, y-15), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 225),2)


cv2.imshow('Result',img)
cv2.waitKey(0)