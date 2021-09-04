import numpy as np
import csv
import os
filename = "data.csv"
fields = ['fileName', 'edge', 'gray', 'haralick','Class'] 
path_haralick_Black = r"D:\1_document\work\softdev_premiumtraning\softdev_premiumtraning\Data_Preprocessing\feature_out\haralick\black"
path_gray_Black= r"D:\1_document\work\softdev_premiumtraning\softdev_premiumtraning\Data_Preprocessing\feature_out\gray\gray_scb"
path_edge_Black =r"D:\1_document\work\softdev_premiumtraning\softdev_premiumtraning\Data_Preprocessing\feature_out\edge\black"
fname_black = os.listdir(path_haralick_Black)

path_haralick_white = r"D:\1_document\work\softdev_premiumtraning\softdev_premiumtraning\Data_Preprocessing\feature_out\haralick\white"
path_gray_white= r"D:\1_document\work\softdev_premiumtraning\softdev_premiumtraning\Data_Preprocessing\feature_out\gray\gray_scw"
path_edge_white =r"D:\1_document\work\softdev_premiumtraning\softdev_premiumtraning\Data_Preprocessing\feature_out\edge\white"
fname_white = os.listdir(path_haralick_white)
with open(filename,'a', newline='') as f: 
    # creating a csv writer object 
    writer = csv.writer(f)
    writer.writerow(fields)

        
    for fname in fname_black:
        haralick = np.load(os.path.join(path_haralick_Black,fname))
        gray = np.load(os.path.join(path_gray_Black,fname))
        edge = np.load(os.path.join(path_edge_Black,fname))
        row_black = [fname,edge,gray,haralick,"black"]
        writer.writerow(row_black)

    for fname1 in fname_white:
        haralick1 = np.load(os.path.join(path_haralick_white,fname1))
        gray1 = np.load(os.path.join(path_gray_white,fname1))
        edge1 = np.load(os.path.join(path_edge_white,fname1))
        row_white= [fname1,edge1,gray1,haralick1,"white"]
        writer.writerow(row_white)
    
    f.close()

