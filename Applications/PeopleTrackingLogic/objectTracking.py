#REFER Tracking objects notebook for further details
import os
import time
import ast
import numpy as np
import cv2
import math
import numpy as np

def get_iou(bb1, bb2):
    try:
        """
        Calculate the Intersection over Union (IoU) of two bounding boxes.

        Parameters
        ----------
        bb1 : dict
            Keys: {'x1', 'x2', 'y1', 'y2'}
            The (x1, y1) position is at the top left corner,
            the (x2, y2) position is at the bottom right corner
        bb2 : dict
            Keys: {'x1', 'x2', 'y1', 'y2'}
            The (x, y) position is at the top left corner,
            the (x2, y2) position is at the bottom right corner

        Returns
        -------
        float
            in [0, 1]
        """
        assert bb1['x1'] < bb1['x2']
        assert bb1['y1'] < bb1['y2']
        assert bb2['x1'] < bb2['x2']
        assert bb2['y1'] < bb2['y2']

        # determine the coordinates of the intersection rectangle
        x_left = max(bb1['x1'], bb2['x1'])
        y_top = max(bb1['y1'], bb2['y1'])
        x_right = min(bb1['x2'], bb2['x2'])
        y_bottom = min(bb1['y2'], bb2['y2'])

        if x_right < x_left or y_bottom < y_top:
            return 0.0

        # The intersection of two axis-aligned bounding boxes is always an
        # axis-aligned bounding box
        intersection_area = (x_right - x_left ) * (y_bottom - y_top )

        # compute the area of both AABBs
        bb1_area = (bb1['x2'] - bb1['x1'] ) * (bb1['y2'] - bb1['y1'] )
        bb2_area = (bb2['x2'] - bb2['x1'] ) * (bb2['y2'] - bb2['y1'] )

        # compute the intersection over union by taking the intersection
        # area and dividing it by the sum of prediction + ground-truth
        # areas - the interesection area
        iou = intersection_area / float(bb1_area + bb2_area - intersection_area)
        assert iou >= 0.0
        assert iou <= 1.0
        return iou
    except AssertionError:
        return 0

vid_file = "data/twoPeopleWalking.mp4"
vid_name = "twoPeopleWalking"
cap = cv2.VideoCapture(vid_file)
frame_array = []
framecount = 0
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('MANUAL_'+vid_name+'.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 30, (frame_width,frame_height))

# Video Capture using OpenCV VideoCapture
start_time = time.time()

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

previousCoordinates = ""
peopleindex = 0
peoplemapping = {}
print("STARTING PROCESS...")
imageArray = os.listdir("Dividedframes")
strPeopleMapping = ""
index = 2

while index < len(imageArray):
    if index == 54:
        index = index + 1
    name = 'Dividedframes/'+'output_twoPeopleWalking_'+str(index)+'.jpeg'
    frame = cv2.imread('Dividedframes/'+'output_twoPeopleWalking_'+str(index)+'.jpeg')
    if frame is not None:
        currentCoordinates = ""
        img1 = frame
        coordinates = previousCoordinates.split("\n")
        coordinates.pop()
        peopleCount = 0

        with open("mloutput/"+'output_output_twoPeopleWalking_'+str(index)+'.jpeg'+".txt") as f:
            newcoordinates = f.read()
        newcoordinates = newcoordinates.split("\n")
        newcoordinates.pop(0)

        for boxes in newcoordinates:
            if boxes is None:
                continue
            else:
                peopleCount  = peopleCount + 1

                boxesarr = boxes.split(" ")
                top = ast.literal_eval(boxesarr[0])
                bottom = ast.literal_eval(boxesarr[1])

                coordinatesStr = {}
                coordinatesStr['x1'] = top[0]
                coordinatesStr['x2'] = bottom[0]
                coordinatesStr['y1'] = top[1]
                coordinatesStr['y2'] = bottom[1]

                topstr = "("+str(coordinatesStr['x1'])+","+str(coordinatesStr['y1'])+")"
                bottomstr = "("+str( coordinatesStr['x2'])+","+str(coordinatesStr['y2'])+")"
                currentValue = str(topstr)+" "+str(bottomstr)
                currentCoordinates = currentCoordinates+str(topstr)+" "+str(bottomstr)+"\n"

                if previousCoordinates != "":

                    bb2 = {}
                    bb2['x1'] = top[0]
                    bb2['x2'] = bottom[0]
                    bb2['y1'] = top[1]
                    bb2['y2'] = bottom[1]

                    currentIou = 0
                    iouIndex = 0
                    for currentIndex,boxes in enumerate(coordinates):
                        boxesarr = boxes.split(" ")
                        top = ast.literal_eval(boxesarr[0])
                        bottom = ast.literal_eval(boxesarr[1])
                        bb1 = {}
                        bb1['x1'] = top[0]
                        bb1['x2'] = bottom[0]
                        bb1['y1'] = top[1]
                        bb1['y2'] = bottom[1]
                        result = get_iou(bb1,bb2)
                        temp = currentIou
                        currentIou = max(result,currentIou)
                        if temp != currentIou:
                            iouIndex = currentIndex
                    if currentIou != 0:
                        peoplemapping[currentValue] = peoplemapping[coordinates[iouIndex]]
                    #check for index:
                    try:
                        if peoplemapping[currentValue]:
                            pass
                    except:
                        peopleindex = peopleindex + 1
                        peoplemapping[currentValue] = peopleindex
                else:
                    try:
                        if peoplemapping[currentValue]:
                            pass
                    except:
                        peopleindex = peopleindex + 1
                        peoplemapping[currentValue] = peopleindex

                # IOU PART - END
                strPeopleMapping = strPeopleMapping+currentValue+":"+str(peoplemapping[currentValue])+"|"
                cv2.rectangle(img1,(coordinatesStr['x1'],coordinatesStr['y1']),(coordinatesStr['x2'],coordinatesStr['y2']), (255,0,0) , 2)
                cv2.putText(img1,"index : "+str(peoplemapping[currentValue]),(coordinatesStr['x1'],coordinatesStr['y1']),cv2.FONT_HERSHEY_DUPLEX,1.0,(0,0,255))

        out.write(img1)
        previousCoordinates = currentCoordinates
        index = index + 1
        print("image count : "+str(index))
        strPeopleMapping = strPeopleMapping+"\n"
    else:
        break

print("FINAL PEOPLEMAPPING IS : "+strPeopleMapping)
with open("peopleMapping.txt","a+") as myfile:
            myfile.write(strPeopleMapping)

elapsed_time = time.time() - start_time
print("Performace measure : "+str(elapsed_time))

# When everything done, release the video capture and video write objects
cap.release()
out.release()
# Closes all the frames
