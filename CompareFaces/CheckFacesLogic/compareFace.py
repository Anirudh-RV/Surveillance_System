# -*- coding: utf-8 -*-

'''
source : https://github.com/12345k/Two-Face-Comparison
To run :
python3 compareFace.py  hardy1face.jpg hardy2face.jpg

face_recognition github : https://github.com/ageitgey/face_recognition
'''
from __future__ import print_function
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
    print("unknown_encodings "+str(unknown_encodings))

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

def checkDataBaseForFaces():
    listofmatches = []
    # img1 will be entry from user
    imgsent = 'imagetest.jpg'
    # get just the face and then start comparing
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # Read the input image
    img = cv2.imread(imgsent)
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
    faceImgsent = "face_"+imgsent
    cv2.imwrite("face_"+imgsent,croppedface)
    listofimages = os.listdir("faceimages")
    for images in listofimages:
        if images != ".DS_Store":
            print("image name :"+images)
            # Load the cascade
            img2 = 'faceimages/'+images
            result = main(faceImgsent,img2)
            if result == True:
                print("Image : "+str(imgsent)+" matches with image : "+str(images))
                listofmatches.append(images[6:])

    print("all matches: \n"+str(listofmatches))

checkDataBaseForFaces()
