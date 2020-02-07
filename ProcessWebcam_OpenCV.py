from darkflow.net.build import TFNet
import cv2
import time
import os
import matplotlib.pyplot as plt
import numpy as np

# To set the directory for easy access.

os.chdir("Desktop/FinalYearProject/Yolo_With_Textboxplusplus")

# To load the model and the weights.

yolo9000 = {"model" : "cfg/yolo9000.cfg", "load" : "yolo9000.weights", "threshold": 0.01}
tfnet = TFNet(yolo9000)

# Video Capture on Webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    framecount = framecount + 1
    ret, frame = cap.read()
    if frame is not None:
        if framecount % 1 == 0:
            result = tfnet.return_predict(frame)
            for res in result:
                if res["label"] == "whole" or res["label"] == "instrumentality" or res["label"] == "chordate":
                    continue
                else:
                    print(res["label"])
                    color = int(255 * res["confidence"])
                    top = (res["topleft"]["x"], res["topleft"]["y"])
                    bottom = (res["bottomright"]["x"], res["bottomright"]["y"])
                    cv2.rectangle(frame, top, bottom, (255,0,0) , 2)
                    #cv2.putText(imgcv, res["label"], top, cv2.FONT_HERSHEY_DUPLEX, 1.0, (0,0,255))

        else:
            # process by skipping frames
            pass

        cv2.imshow('OUTPUT', frame)
        frame_array.append(frame)
        c = cv2.waitKey(1)
        if c == 27:
            break
    else:
        break


cap.release()
cv2.destroyAllWindows()
