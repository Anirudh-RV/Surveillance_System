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
