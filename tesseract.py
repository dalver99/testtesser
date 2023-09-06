import cv2
import pytesseract

img = cv2.imread('image.jpg')

# Get verbose data including boxes, confidences, line and page numbers
hocr = pytesseract.image_to_pdf_or_hocr('image.jpg', extension='hocr', lang='kor')

# Print hocr to see the result
print(hocr)