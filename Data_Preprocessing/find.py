import cv2
import os
import numpy as np
def nothing(x):
    pass
cv2.namedWindow("Trackbar")
cv2.createTrackbar("lh","Trackbar",0,255,nothing)
cv2.createTrackbar("lv","Trackbar",0,255,nothing)
cv2.createTrackbar("ls","Trackbar",0,255,nothing)
cv2.createTrackbar("uh","Trackbar",0,255,nothing)
cv2.createTrackbar("us","Trackbar",0,255,nothing)
cv2.createTrackbar("uv","Trackbar",0,255,nothing)

#Trackbar HSV COlOR
while True:
    path_screw_black = r"D:\1_document\internship\dataset"
    path_screw_white = r"D:\1_document\work\softdev_premiumtraning\softdev_premiumtraning\Data_Preprocessing\feature_out\clean_imageData\black"
    name = os.listdir(path_screw_white)
    img = cv2.imread(os.path.join(path_screw_white,name[0]),0)
    # HSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #GET value frome trackbar
    lh = cv2.getTrackbarPos("lh","Trackbar")
    print(lh)
    ls = cv2.getTrackbarPos("ls","Trackbar")
    lv = cv2.getTrackbarPos("lv","Trackbar")
    uh = cv2.getTrackbarPos("uh","Trackbar")
    us = cv2.getTrackbarPos("us","Trackbar")
    uv = cv2.getTrackbarPos("uv","Trackbar")
    # HSV_value = np.array([[ls,lh,lv],[uh,us,uv]])
    #forst mask

    # lower = np.array([lh,ls,lv])
    # upper = np.array([uh,us,uv])
    tresh = np.array([lh,ls])
    ret,thresh_binary = cv2.threshold(img,lh,ls,cv2.THRESH_BINARY)
    # mask = cv2.inRange(img,lower,upper)
    # kernel= np.ones((5, 5))
    # mask= cv2.erode(mask,kernel)
    
    # cv2.imshow("image",img)
    # cv2.imshow("HSV",HSV)
    # cv2.imshow("mask",mask)
    cv2.imshow("",thresh_binary)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        np.savetxt('tresh_value_black.txt',tresh,delimiter=',')
        break



