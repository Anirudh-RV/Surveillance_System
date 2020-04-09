import os
import cv2
import numpy as np
import requests
from html.parser import HTMLParser
import urllib.request
import json

listofimages = []
response = requests.post('http://localhost:8080/getimages',data = "CompareFaceDatabase")
JsonResponse = json.loads(response.text)
imagenames = JsonResponse["data"]
listofimages = imagenames.split("</br>")
listofimages.pop()
print("list: ")
print(listofimages)

for images in listofimages:
    if images != ".DS_Store":
        print("image name :"+images)
        # Load the cascade
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        # Read the input image
        url = "http://localhost:4000/comparefaces/"+images

        req = urllib.request.urlopen(url)
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        img = cv2.imdecode(arr, -1) # 'Load it as it is'

        # Convert into grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw rectangle around the faces
        #  crop_img = img[res["topleft"]["y"]:res["bottomright"]["y"],res["topleft"]["x"]:res["bottomright"]["x"]]
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            break

        crop_img = img[y:y+h,x:x+w]
        crop_img = crop_img.copy()
        crop_img = cv2.resize(crop_img, dsize=(512, 512), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite('../CompareFaces/mlbackend/assets/faceimages/faces_'+images,crop_img) # can remain the same
        print("writing: "+str('faceimages/faces_'+images))
