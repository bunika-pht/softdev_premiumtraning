import os
import cv2 as cv
import numpy as np
import math
import matplotlib
x=0
y=0
w=0
h =0

path_screw_black = r"D:\1_document\internship\dataset"
path_screw_white = r"D:\1_document\internship\dataset12\dataset"
output= r"D:\1_document\work\softdev_premiumtraning\softdev_premiumtraning\Data_Preprocessing\feature_out\gray_scw"

value =np.loadtxt('HSV_value_white.txt',dtype='int',delimiter=',')
name_black = os.listdir(path_screw_black)
name_white = os.listdir(path_screw_white)

# pic = cv.imread(os.path.join(path_screw_black,name_black[0]))
# HSV = cv.cvtColor(pic,cv.COLOR_BGR2HSV)
# lower = np.array([value[0][0],value[0][1],value[0][2]])
# upper = np.array([value[1][0],value[1][1],value[1][2]])
# mask = cv.inRange(HSV,lower,upper)
# kernel= np.ones((5, 5))
# mask= cv.erode(mask,kernel)
# mask = cv.bitwise_not(mask)
# contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# if len(contours) > 0:
#     area = max(contours,key=cv.contourArea)
#     x,y,w,h = cv.boundingRect(area)
# frame = pic.copy()
# cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)    
# img_crop = pic[y:y+h, x:x+w]
# cv.imshow("",img_crop)

# cv.waitKey(0)
for fname in name_white:
    pic = cv.imread(os.path.join(path_screw_white,fname))
    HSV = cv.cvtColor(pic,cv.COLOR_BGR2HSV)
    lower = np.array([value[0][0],value[0][1],value[0][2]])
    upper = np.array([value[1][0],value[1][1],value[1][2]])
    mask = cv.inRange(HSV,lower,upper)
    kernel= np.ones((5, 5))
    mask= cv.erode(mask,kernel)
    # mask = cv.bitwise_not(mask)
    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        area = max(contours,key=cv.contourArea)
        x,y,w,h = cv.boundingRect(area)
    frame = pic.copy()
    cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)    
    img_crop = pic[y:y+h, x:x+h]
    resized = cv.resize(img_crop,(500,500))
    out= os.path.splitext(os.path.join(output,fname))[0]
    edges_of_image = cv.Canny(resized,0,50) 
   
    gray = cv.cvtColor(resized,cv.COLOR_BGR2GRAY)
    np.save(out+'.npy',gray)
    # np.save(out+'.npy',gray)
# for fname in name_white:
#     pic = cv.imread(os.path.join(path_screw_white,fname),0)
#     out= os.path.splitext(os.path.join(output,fname))[0]
#     print(out)
#     np.save(out+'.npy',pic)

# data =np.load(r"Data_Preprocessing\feature_out\treshold\frame (1).npy")
# print(data)