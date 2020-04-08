# Introduction to Surveillance_System

# NOTE - Main App functions
1. Compare Face Frontend
2. Download Youtube Video and divide it
3. Annotation function
4. Seeing Live Camera Feed

# NOTE - Functions with Django/Flask
1. Running yolo/Textbox++ for IoU in Django (Port:8000)
2. Running Yolo-indexing /Textbox++/ Integrated Yolo-Indexing and Textbox++/ yolo-indexing-peoplematching on Flask (Port:5000)
3. Running Compare Faces in the backend in Django (Port:9000)

# NOTE
1. yolo-indexing and textbox++ are already integrated, add peoplematching component to obtain final flask application
2. Django and CompareDjango are run on 8000 and 9000 ports

3. Finally, the frontend should function and backends with 8000,9000 and 5000 ports should function
# Technologies used
1. ReactJs for Frontend (3000)
2. NodeJs for Backend (4000)
3. Django to run the Machine learning algorithms in the background (8000)
4. Golang for running GO API's to connect the application with the Database (8080)
5. MongoDB as NoSQL Database (27017)
6. OpenCV for drawing boxes and checking IoU and for dividing the video into frames
7. DarkFlow for running yolo9000
8. tensorflow, numpy, keras for assisting the machine learning application
9. matplotlib is being used for testing images (display of images)
10. Vanilla Js for functions and bits of React code
11. face_recognition library for detecting faces
12. face_recognition library for comparing faces
13. OpenCV haarcascades for detecting faces
14. Flask for livestreaming (5000)
15. Docker

# How it works

# Dockerized Apps :

**Resources :**
https://docs.docker.com/docker-for-mac/
https://docs.docker.com/compose/gettingstarted/
https://medium.com/travis-on-docker/how-to-dockerize-your-go-golang-app-542af15c27a2

**Important INFO :**
1. Once the frontend/Webapp is comlpetely dockerized
2. Need to check with Django/CompareDjango/CropFaces/LiveStreamingOutput/PeopleAnomalyDetection
3. Need to make sure that the dockerized application still functions the way it is supposed with
all the integrations done
4. Verify all features worked on are avaiable in the final version


**Important**
1. lsof -P | grep ':4000' | awk '{print $2}' | xargs kill -9

2. Problem with API_Go : Until a static IP Address for the mongodb server is not found, for each system
the user has to build the API_Go container by changing the IP Address to their Computer IP in
  a. HandleUsers/UserFunc.go
  b. HandleImages/ImageFunc.go

**To run from docker  :(Build Inside respective folders)**

**Start MongoDB**
1. Local: docker run -d -p 27017-27019:27017-27019 --name mongodb mongo
(or)
1. Local: docker run -d -p 27017-27019:27017-27019 --name <CONTAINER ID> mongo

2. Important : Make sure mongo is running on <ip-address>:27017 before running GO API

**To run GO API**
1. To build: docker build -t anirudhrv1234/goapi .

2. Remote: docker run --rm -it -p 8080:8080 anirudhrv1234/goapi

3. Local: docker run --rm -p 8080:8080 anirudhrv1234/goapi

**To run NodeServer (Node JS)**
1. Local: docker run -p 4000:4000 anirudhrv1234/nodeserver

**To run Client (React JS)**
1. To build: docker build -t anirudhrv1234/reactjs .

2. Local: docker run -p 3000:3000 anirudhrv1234/reactjs

**Commands to run a Docker app (GENERAL):**

**To make directory :**
1. mkdir test
2. cd test

**To make the app :**
1. touch myapp.py
2. open myapp.py
3. -Copy & Paste the required code

**To define the requirements/dependencies :**
1. touch requirements.txt
2. open requirements.txt
3. -Copy & Paste the required dependencies

**To create Dockerfile**
1. touch Dockerfile
2. open Dockerfile
3. -Copy & Paste the system configuration

**To create docker-compose.yml**
1. touch docker-compose.yml
2. open docker-compose.yml
3. -Copy & Paste the required configuration

**Run the App**
1. docker-compose up

**To delete images**
1. docker system prune

# DetectingAnamolyPeople
A security system which helps in detecting people from a given set in real time

**Explanation of module :**
1. A person's photo can be uploaded using the web app provided through the frontend
2. The user's have to be signed in to access this feature
3. Once the picture has been uploaded, periodically cropjustface.py is run in order to update the database
4. Once the database is updated, the person can be tracked
5. The streamingserver i.e the Flask app which process the video and shows the output live process and tracks the person
6. The person is first identified using the yolo algorithm
7. Then from the cropped person's body, the face is retrieved using face_recognition library
8. It is then compared with every other person in the database and checked for similarities
9. If a similarity exists, then the person will be bound with a green box
10. Else, the person will be bound with a red box


# Recognising people
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

# Live Streaming
**Streaming Output (Changes to this need to be made)**
1. Using a flask backend to stream data from a security camera
2. Displaying it live on a url
3. Further changes and modifications can be made to the frames

# Measuring IoU
**Process of measuring IoU**
1. Each bounding box with label : "people" is considered (Iterated through)
2. The bounding box is checked with all the ground truths for IoU
3. The maximum IoU is considered for that bounding box (non-max suppression)
4. The above process is repeated for each bounding box detected by the YOLO algorithm
5. To add the possibility that people in the ground truth are completely ignored by the yolo algorithm
  a.The difference between the number of people detected by yolo and the number of people annotated for ground truth is considered
  b.This is added as extra 0's to the list of the IoU's
6. The average of all the maximum IoU's of each bounding box and the additional 0's is taken for overall IoU for an image
7. The average of all the IoU's for each image is taken as the average IoU for the dataset (~400 images)
8. check code in CheckIoU/iou.py for source code

# Tracking People
**Tracking People / Object Indexing :**
1. Initialise detected people to 0
2. When the processing of the frames start, each box that is detected by the yolo algorithm
is compared to all previous detected boxes. As we initialised detected people people to 0,
3. All the newly detected boxes are considered as new people and the people count is increased,
and each box is indexed with a unique number (here, just the people count)
4. During the next Iteration of the processing, all the detected boxes are compared to previously detected boxes
and the IoU between the boxes is calculated,
5. If there is a high IoU between a previous box and the current box being processed, we consider that the same person
has moved from the previous frame, hence the IoU is high and the new box is given the index of the previous detected box
6. When we repeat the above steps, it tracks people's movements through and the frames and hence we can tracking people
when they are in front of a particular camera
7. When a newly detected box has 0 IoU with all the previously detected boxes, we classify that as a new person,
increase the people count and index the person
8. If an old box has no overlaps with any of the new boxes, it is discarded

*NOTE:*
The assumption taken here is that, when people move from one position in front of the camera to another or if there is a
continuous movement of the people, as the video is divided into frames, the person under consideration will move
slowly between these frames and the box around them also moves slowly with them.
Therefore, if we can measure the IoU of the boxes between frames, we can figure out which boxes are moving and where they
are moving and which direction they are moving.
This gives us an idea of the traffic in front of the camera and also gives us valuable data regarding how long a
person or a group of people stay in front of the camera.
As an example,
1. If we detect around 4 people who have the same index being in the coverage of the camera for a very long
time, we can raise an alert
2. If we know the daily traffic in front of a camera and the number of people abruptly increases / abruptly decreases
we can raise an alert
3. If we detect objects like a suitcase being in front of a camera for too long, we can raise an alert as the algorithm
gets to know, it is the same suitcase as a result of the object indexing

*Draw backs of the algorithm :*
1. The algorithm is too sensitive to change and the yolo algorithm does not provide the required accuracy to make the
algorithm work perfectly.
2. When there are crowded areas and the boxes overlap when detection happens, there are chances that the index of the
person jumps between people

*Improving the algorithm :*
1. A better object detection algorithm might improve the performance of the object tracking
2. To make the algorithm a lot less sensitive to change and have a better more strict policy to change the
index of a person
3. Finding a better metric than IoU to find if a box is moving between frames

# Video Download
**Downloading and processing video :**
1. If a video is already available, place it in the main folder or download a video from YouTube(Y2 downloader or In-House application)
2. Run the dividevideo.py to split the video into frames at random intervals between 2-5 seconds (considering 30 fps)
3. The divided frames will be available in the Dividedframes folder

# Annotation System
**Annotation System :**
1. The user signs up into the system by giving email,username,name and password
2. Once the signUp is successful, the user is redirected to the upload page
3. The user can upload upto 99 images at once and click viewimages
4. Upon succeful upload of the images, the user is redirected to the EditPage
5. EditPage contains the NavigationBar and the WorkingArea
6. The user can draw boxes around the subject of interest and click save
7. Upon clicking save, the coordinates of the boxes drawn will be saved in the backend
8. The User has two options to check the IoU :
  a. Check IoU at each image :
    1. The user can click on Check ml output yolo to check the IoU for that particular file
    2. Continue this process for each image and the individual IoU's will be saved in the IoU folder in IoU.txt
    3. Download/DownloadAll depending on the nature of output needed
      I.Download will only download the annotations
      II.DownloadAll will download the images,mloutputs,annotations,IoU and any aditional data present
  b. Continue the annotations for all images and check IoU together
    1. The user can just keep annotating images to have a smooth workflow
    2. DownloadAll once the annotations are done
    3. Place the images and the output in the checkIoU folder
    4. Run iou.py to check the IoU of all images and store it in the IoU folder in IoU.txt
9. The output of the machine learning algorithms can be seen by running checkmloutput.py, images will be stored in the mlimages folder

**System Architecture**
system_architecture.jpeg

**IOU**
1. For people label on dataset collected from mainly Indian sources : 0.3005834618310959
2. Number of images in test data : 381

# How to run
**Steps to run the application (may involve downloading mongo,go libraries and setting up django environment)**
1. clone the git
2. Download both weights from :
  1. https://drive.google.com/drive/folders/1pW4mKNOzOIf0Edyr4BppwnLpddCQ6Qch?usp=sharing

  2. https://drive.google.com/open?id=1JupZYcQO7Jh5aiRQLwNzYZaX0uYGULdK

3. Place the weights in the Django/mlbackend folder with the other .py files

Reactjs : 3000
1. cd Client
2. npm install
3. npm start

Go API: 8080
1. cd API_Go
2. go run main.go

Django: 8000
1. cd django
2. cd mlbackend
3. python3 manage.py runserver

Django: 9000
1. cd django
2. cd mlbackend
3. python3 manage.py runserver <port-number> : 9000

NodeServer: 4000
1. cd NodeServer
2. node server.js

Flask : 5000
python3 Lstreamoutput.py

**if npm build is failing, install by : npm install <absent library>**

For building yolo9000 :
1. pip install Cython
2. git clone https://github.com/thtrieu/darkflow.git
3. cd darkflow
4. python3 setup.py build_ext --inplace
5. pip install .
**anywhere in the system**

To get mongo working :
1. use GoDB
2. db.createCollection("ImageNames")
3. db.createCollection("UserData")

**Surveillance_System**
1. Install DarkNet
2. Install Cython
3. Download both weights from :

https://drive.google.com/drive/folders/1pW4mKNOzOIf0Edyr4BppwnLpddCQ6Qch?usp=sharing

https://drive.google.com/open?id=1JupZYcQO7Jh5aiRQLwNzYZaX0uYGULdK

4. Can either Clone the directory or download the ZIP file from the above link.
5. Run FinalYearNoteBook.ipynb and see the project.
6. Edit the directory in the notebook according to your system.
