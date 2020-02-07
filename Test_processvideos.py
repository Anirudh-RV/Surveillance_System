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
# Video to Frames.

directory_input = "data/"
video_name = "TestVid.mp4"
directory_output = "data/Frames/"
output_name = "output_frames_"

video_to_frames = "ffmpeg -i "+directory_input+video_name+" -vf fps=30 "+directory_output+output_name+"%d.png"
print(video_to_frames)
os.system(video_to_frames)

# To run frames stored.

count = 1
prefix = "data/Frames/"
for i in os.listdir('data/Frames'):
    if i == '.DS_Store':
        pass
    else:
        start_time = time.time()
        img = prefix+i
        print("Input : ")
        print(img)
        imgcv = cv2.imread(img)
        result = tfnet.return_predict(imgcv)
        for res in result:
            if res["label"] == "whole":
                continue
            else:
                color = int(255 * res["confidence"])
                top = (res["topleft"]["x"], res["topleft"]["y"])
                bottom = (res["bottomright"]["x"], res["bottomright"]["y"])
                cv2.rectangle(imgcv, top, bottom, (255,0,0) , 2)
                #cv2.putText(imgcv, res["label"], top, cv2.FONT_HERSHEY_DUPLEX, 1.0, (0,0,255))

        print("Output : ")
        print("data/Result_Frames/"+i)
        cv2.imwrite("data/Result_Frames/"+i, imgcv)
        count = count + 1
        elapsed_time = time.time() - start_time
        print("Performace measure : "+str(elapsed_time))

# Frames to Video.

directory_input = "data/Result_Frames/"
frame_name = "output_frame_test"
directory_output = "data/Result_Videos/"
output_video = "output_video_quick1"

frames_to_video = "ffmpeg -start_number 1 -i "+directory_input+frame_name+"%d.png -c:v libx264 -vf fps=30 -pix_fmt yuv420p "+directory_output+output_video+".mp4"
print(frames_to_video)
os.system(frames_to_video)
