import cv2 
import numpy as np 
"""
cv.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
cv.IMREAD_GRAYSCALE : Loads image in grayscale mode
cv.IMREAD_UNCHANGED : Loads image as such including alpha channel
just pass -1,0,1 for reading in specific mode
""" 
img=cv2.imread("/home/ashifer/code/opencv_/samp.png")  
img_grey=cv2.imread("/home/ashifer/code/opencv_/samp.png",0) 
img_unc=cv2.imread("/home/ashifer/code/opencv_/samp.png",1) 
cv2.imshow('image',img_unc)#first arg is window title   
cv2.waitKey(0)#waits in ms if 0 waits for keyboard intrpt   
cv2.destroyAllWindows()  
cv2.imshow("image_greyscale",img_grey)  
key=cv2.waitKey(0) 
if key==ord('s'): 
    #cv2.imwrite("greyscales.png",img_grey) #saves images   
    cv2.destroyAllWindows()  
else:
    cv2.destroyAllWindows() 
#using matplots 
from matplotlib import pyplot as plt
img = cv2.imread("/home/ashifer/code/opencv_/samp.png",0)
plt.imshow(img, cmap = 'gray',interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis 
plt.show() 
