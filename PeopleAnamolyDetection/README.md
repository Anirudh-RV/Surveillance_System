# DetectingAnamolyPeople
A security system which helps in detecting people from a given set in real time

# Explanation of module :

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

# TEMPLATE FOR MERN WEBAPP, USES GO AND DJANGO  

# How to run
Reactjs : 3000
1. cd Client
2. npm install
3. npm start

Go API: 8080
1. cd API_Go
2. go run main.go

Django: 8000
1. cd pythonbackend
2. cd djangobackend
3. python3 manage.py runserver

NodeServer: 4000
1. cd NodeServer
2. node server.js

**if npm build is failing, install by : npm install <absent library>**

**anywhere in the system**
To get mongo working :
1. use GoDB
2. db.createCollection("ImageNames")
3. db.createCollection("UserData")

# To run StreamingServer

1. Python3 LstreamoutputYI.py
