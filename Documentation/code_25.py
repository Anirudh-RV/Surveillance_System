# To import libraries for Yolo-90000.

from darkflow.net.build import TFNet
import cv2
import time
import os
import matplotlib.pyplot as plt
import numpy as np

# To import PyTesseract
import pytesseract

# To set the directory for easy access.

os.chdir("Desktop/FinalYearProject/Yolo_With_Textboxplusplus")

# To load the model and the weights.

yolo9000 = {"model" : "cfg/yolo9000.cfg", "load" : "yolo9000.weights", "threshold": 0.01}
tfnet = TFNet(yolo9000)

# To run single photo and save each box.

start_time = time.time()

img = "data/peopletext1.jpeg"
imgname = "peopletext1.jpeg"

imgcv = cv2.imread(img)
plt.imshow(imgcv)
plt.show()

result = tfnet.return_predict(imgcv)
count = 1

cv2.imwrite("results/Orginial_"+str(imgname), imgcv)

for res in result:
    if res["label"] == "whole":
        continue
    else:
        color = int(255 * res["confidence"])
        top = (res["topleft"]["x"], res["topleft"]["y"])
        bottom = (res["bottomright"]["x"], res["bottomright"]["y"])
        # for each person
        print(top)
        print(bottom)
        crop_img = imgcv[res["topleft"]["y"]:res["bottomright"]["y"],res["topleft"]["x"]:res["bottomright"]["x"]]

        print(res["label"])
        if len(crop_img) != 0:
            #cv2.imwrite("results/crop_"+res["label"]+"_"+str(count)+"_"+str(imgname), crop_img)
            print("results/crp_"+res["label"]+"_"+str(count)+str(imgname))
            plt.imshow(crop_img)
            plt.show()



        cv2.rectangle(imgcv, top, bottom, (255,0,0) , 2)
        #cv2.putText(imgcv, res["label"], top, cv2.FONT_HERSHEY_DUPLEX, 1.0, (0,0,255))
        print(count)
    count = count + 1


cv2.imwrite("data/Result/Final_"+str(imgname), imgcv)
elapsed_time = time.time() - start_time
print("Performace measure : "+str(elapsed_time))

#print (result) result of all boxes.

plt.imshow(imgcv)
plt.show()

cv2.imwrite("results/Result.jpg", imgcv)

# To make frames.

# Command to make videos to frames : ffmpeg -i TestVid.mp4 -vf fps=30 Frames/out%d.png

# Command to make frames to videos : ffmpeg -start_number 1 -i Frames/out%d.png -c:v libx264 -vf fps=30 -pix_fmt yuv420p out.mp4

# Code to run Commands in python : os.system("ffmpeg -i TestVid.mp4 -vf fps=30 Frames/out%d.png")

# TEST MODULE TO : CONVERT VIDEO TO FRAME -> RUN THE FRAMES ON YOLO -> CONVERT THE FRAMES BACK TO VIDEO.

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

# Video capture using Video(OpenCV),WebCam,URL (remote video capture)
# variables
vid_file = "data/pleasework.mp4"
vid_name = "pleasework"
cap = cv2.VideoCapture(vid_file)
frame_array = []
framecount = 0

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 30, (frame_width,frame_height))

# Video Capture using OpenCV VideoCapture
start_time = time.time()

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    framecount = framecount + 1
    ret, frame = cap.read()
    if frame is not None:
        if framecount % 2 == 0:
            result = tfnet.return_predict(frame)
            for res in result:
                if res["label"] == "whole" or res["label"] == "instrumentality" or res["label"] == "chordate":
                    continue
                else:
                    color = int(255 * res["confidence"])
                    top = (res["topleft"]["x"], res["topleft"]["y"])
                    bottom = (res["bottomright"]["x"], res["bottomright"]["y"])
                    cv2.rectangle(frame, top, bottom, (255,0,0) , 2)
                    #cv2.putText(imgcv, res["label"], top, cv2.FONT_HERSHEY_DUPLEX, 1.0, (0,0,255))

        else:
            # process by skipping frames
            pass


        frame_array.append(frame)
        out.write(frame)

        c = cv2.waitKey(1)
        if c == 27:
            break
    else:
        break


elapsed_time = time.time() - start_time
print("Performace measure : "+str(elapsed_time))

# When everything done, release the video capture and video write objects
cap.release()
out.release()

# Closes all the frames

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

# To read from PyTesseract
transcript = pytesseract.image_to_string(Image.open('Desktop/SamsungResearch/Algorithm/Yolo/IndiResult/sample10_1.jpg'), lang='eng').upper()
print(transcript)
