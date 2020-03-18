
import cv2
import numpy as np
img = cv2.imread('test.jpg')
img = cv2.resize(img,(512,512))

img = np.expand_dims(img, axis=0)
print(img.shape)
