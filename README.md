# testtesser

Simple code to read Korean from Tesseract.
Mask the text image with png for UI interactions (POC).

https://github.com/UB-Mannheim/tesseract/wiki

download and install tesseract, then add location to PATH
should look something like

C:\Program Files\Tesseract-OCR

install libraries
pip install beautifulsoup4
pip install lxml

and other stuffs...

Run tesseract first, then paste coordinates to image.py to create a mask image. If you want to decode to Korean, use decode.

![image](https://github.com/dalver99/testtesser/assets/93179574/de0c62b7-9149-4d65-b72b-09c235851785)

This is test result, probably need better image for quality, or more training with trainset. I used raw tesseract.
