# Introduction to ImageAnnotationIoUTool

#Technologies used
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

#How it works

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

**Downloading and processing video :**
1. If a video is already available, place it in the main folder or download a video from YouTube(Y2 downloader or In-House application)
2. Run the dividevideo.py to split the video into frames at random intervals between 2-5 seconds (considering 30 fps)
3. The divided frames will be available in the Dividedframes folder

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

**LOC and program list if needed :**
1. main.go : 437
2. CustomRouting.js : 53
3. EditPage.js : 23
4. Error.js : 27
5. Footer.js : 14
6. Home.js : 17
7. IntroBar.js : 197
8. Routes.js : 63
9. Signin.js : 73
10. SignUp.js : 233
11. Test_Cookies.js : 53
12. TestApi.js : 282
13. TestDjango.js : 46
14. TestNodeApi.js : 116
15. UploadMultipleFiles.js : 164
16. WorkingArea.js : 257
17. Views.py : 320
18. Server.js : 127
19. checkmloutput.py : 45
20. iou.py : 177
21. dividevideo.py : 68

LOC : 2812
