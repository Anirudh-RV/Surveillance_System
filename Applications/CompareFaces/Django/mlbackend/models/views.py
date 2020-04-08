from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.template import Context, loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.template import Context, loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt

import ast
import requests
import time
import PIL
from PIL import Image
from io import BytesIO
import numpy as np

'''
source : https://github.com/12345k/Two-Face-Comparison
To run :
python3 compareFace.py  hardy1face.jpg hardy2face.jpg
face_recognition github : https://github.com/ageitgey/face_recognition
Dlib : http://dlib.net/
'''
import os
import re
import scipy.misc
import warnings
import face_recognition.api as face_recognition
import sys
import cv2

def scan_known_people(known_people_folder):
    known_names = []
    known_face_encodings = []

    basename = known_people_folder
    img = face_recognition.load_image_file(known_people_folder)
    encodings = face_recognition.face_encodings(img)
    if len(encodings) == 1:
        known_names.append(basename)
        known_face_encodings.append(encodings[0])
    return known_names, known_face_encodings

def test_image(image_to_check, known_names, known_face_encodings):
    unknown_image = face_recognition.load_image_file(image_to_check)

    # Scale down image if it's giant so things run a little faster
    if unknown_image.shape[1] > 1600:
        scale_factor = 1600.0 / unknown_image.shape[1]
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            unknown_image = scipy.misc.imresize(unknown_image, scale_factor)

    unknown_encodings = face_recognition.face_encodings(unknown_image)

    if len(unknown_encodings)==1:
        for unknown_encoding in unknown_encodings:
            result = face_recognition.compare_faces(known_face_encodings, unknown_encoding)
            distance = face_recognition.face_distance(known_face_encodings, unknown_encoding)
            print(distance[0])
            print("True") if True in result else print("False ")

        return distance[0],result[0]
    else:
        return "0","Many Faces or No Faces"

def image_files_in_folder(folder):
    return [os.path.join(folder, f) for f in os.listdir(folder) if re.match(r'.*\.(jpg|jpeg|png)', f, flags=re.I)]

def main(known_people_folder, image_to_check):
    known_names, known_face_encodings = scan_known_people(known_people_folder)
    distance,result=test_image(image_to_check, known_names, known_face_encodings)
    return result

@csrf_exempt
def index(request):
    decodeddata = request.body.decode('utf-8')
    dictdata = ast.literal_eval(decodeddata)
    username = dictdata["username"]
    imagename = dictdata["imagename"]
    imageurl = dictdata["imageurl"]

    start_time = time.time()
    # getting the image
    print("UserName : "+str(username))
    print("ImageName : "+str(imagename))
    print("imgeurl : "+str(imageurl))

    url = imageurl
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = np.array(img)
    saveimageindjango = 'assets/peopleimages/'+imagename
    cv2.imwrite(saveimageindjango, img)
    img_h = img.shape[0]
    img_w = img.shape[1]
    imgcv = cv2.imread(saveimageindjango)

    listofmatches = []
    # img1 will be entry from user
    imgsent = imagename
    # get just the face and then start comparing
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # Read the input image
    img = cv2.imread('assets/peopleimages/'+imgsent)
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
    croppedface = cv2.resize(crop_img, dsize=(512, 512), interpolation=cv2.INTER_CUBIC)
    faceImgsent = "assets/tempfaces/face_"+imgsent
    cv2.imwrite(faceImgsent,croppedface)
    listofimages = os.listdir("assets/faceimages")

    for images in listofimages:
        if images != ".DS_Store":
            print("image name :"+images)
            # Load the cascade
            img2 = 'assets/faceimages/'+images
            result = main(faceImgsent,img2)
            if result == True:
                print("Image : "+str(imgsent)+" matches with image : "+str(images))
                listofmatches.append(images[6:])

    print("all matches after: \n"+str(listofmatches))
    print("Backend Process Complete")
    elapsed_time = time.time() - start_time
    print("Performace measure : "+str(elapsed_time))
    context = {"data":listofmatches}
    return render(request, 'index.html', context)

@csrf_exempt
def runmodel(request):
    context = {"data":"data"}
    return render(request, 'index.html', context)
