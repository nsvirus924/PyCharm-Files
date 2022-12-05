import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread("D:\\123456789.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#print(pytesseract.image_to_string(img))

cv2.imshow('result',img)
cv2.waitKey(0)
