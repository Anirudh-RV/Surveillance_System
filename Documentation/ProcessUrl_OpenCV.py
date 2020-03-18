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


# Video Capture on URL (Not Working.)

url = "https://www.earthcam.com/usa/newyork/timessquare/?cam=tstwo_hd"
vid_file = "data/TestVid.mp4"

# Open a sample video available in sample-videos
vcap = cv2.VideoCapture(vid_file)
#if not vcap.isOpened():
#    print "File Cannot be Opened"

while(True):
    # Capture frame-by-frame
    ret, frame = vcap.read()
    #print cap.isOpened(), ret
    if frame is not None:
        # Display the resulting frame
        cv2.imshow('frame',frame)
        # Press q to close the video windows before it ends if you want
        if cv2.waitKey(22) & 0xFF == ord('q'):
            break
    else:
        print ("Frame is None")
        break

# When everything done, release the capture
vcap.release()
cv2.destroyAllWindows()
print ("Video stop")
