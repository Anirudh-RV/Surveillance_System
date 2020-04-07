# Implementation Mechanism :
The process of Recognising people is done with two separate steps :
1. Cropping out the face from the body of a person which yolo has recognised
2. Comparing a given face with the faces already stored in the backend

**1. Cropping out the face from the body of a person which yolo has recognised**

1. The boxes which have the label "people" are stored in the backend and periodically a script is run to
find the faces of the people in those boxes (The boxes bound the body of the person)
2. The boxes around the people help in increasing the accuracy and decreasing the workload on the algorithm
to recognise just faces as it has to go through less complex structures in images
3. cropjustface.py is run through the database to provide the images of just faces
    a. This uses haarcascade_frontalface_default.xml set of weights
    b. The weights are pre-trained and it can recognise faces and puts a bounding box around it
4. These face images are stored separately

**2. Comparing a given face with the faces already stored in the backend**

1. When a particular image is being uploaded onto the webapp to check for similarities
2. The image goes through the NodeServer and is stored in the backend
3. The Django server then reads the URL where the image is stored and processes by using cropjustface algorithm to retrieve just the face.
4. This image is then checked with every other face stored in the backend
5. Each set of image is compared using the face_recognition library and an encodings matrix is formed
6. The similarities between the encoding matrices of the User image and the backend image is calculated
7. If the similarity is above a certain threshold / if the difference between the matrices below a certain
threshold
8. Then, the images are said to be similar and a True boolean value is returned
9. All the URLs of the images which are similar are sent to the front end
8. These URLs are read in the frontend and displayed on the webApp

**Resources**
1.  https://github.com/ageitgey/face_recognition
2.  http://dlib.net/
3.  https://github.com/opencv/opencv/tree/master/data/haarcascades

starter code :
1. https://towardsdatascience.com/face-detection-in-2-minutes-using-opencv-python-90f89d7c0f81
2. https://github.com/12345k/Two-Face-Comparison

# To RUN
**Reactjs : 3000**
1. cd Client
2. npm install
3. npm start

**Go API: 8080**
1. cd API_Go
2. go run main.go

**Django: 8000**
1. cd pythonbackend
2. cd djangobackend
3. python3 manage.py runserver

**NodeServer: 4000**
1. cd NodeServer
2. node server.js

**Server program :**
1. Run cropjustface.py in a constant loop between intervals to process more images that are being uploaded
