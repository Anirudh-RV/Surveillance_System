import pytesseract

# To read from PyTesseract
transcript = pytesseract.image_to_string(Image.open('Desktop/SamsungResearch/Algorithm/Yolo/IndiResult/sample10_1.jpg'), lang='eng').upper()
print(transcript)
