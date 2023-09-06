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

