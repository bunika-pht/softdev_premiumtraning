import numpy as np
import csv
import os


filename = "Dataset/data_new_no_fileformat.csv"
fields = ['fileName']

path_haralick_Black = r"D:/1_document/work/ML program/softdev_premiumtraning/Data_Preprocessing/feature_out/haralick/black"
path_gray_Black = r"D:/1_document/work/ML program/softdev_premiumtraning/Data_Preprocessing/feature_out/gray/gray_scb"
path_edge_Black = r"D:/1_document/work/ML program/softdev_premiumtraning/Data_Preprocessing/feature_out/edge/black"
fname_black = os.listdir(path_haralick_Black)

path_haralick_white = r"D:/1_document/work/ML program/softdev_premiumtraning/Data_Preprocessing/feature_out/haralick/white"
path_gray_white = r"D:/1_document/work/ML program/softdev_premiumtraning/Data_Preprocessing/feature_out/gray/gray_scw"
path_edge_white = r"D:/1_document/work/ML program/softdev_premiumtraning/Data_Preprocessing/feature_out/edge/white"
fname_white = os.listdir(path_haralick_white)
with open(filename, 'a', newline='') as f:
    # creating a csv writer object
    writer = csv.writer(f)

    sample_file = fname_black[0]
    haralick = np.load(os.path.join(path_haralick_Black, sample_file)).tolist()
    gray = np.load(os.path.join(path_gray_Black, sample_file)).tolist()
    edge = np.load(os.path.join(path_edge_Black, sample_file)).tolist()
    feature = haralick+gray+edge

    for i in range(1, len(feature)+1):
        fields.append(str(i))
    fields.append(str("class"))

    writer.writerow(fields)
    for fname in fname_black:
        haralick = np.load(os.path.join(path_haralick_Black, fname)).tolist()
        gray = np.load(os.path.join(path_gray_Black, fname)).tolist()
        edge = np.load(os.path.join(path_edge_Black, fname)).tolist()
        row_black = haralick+gray+edge
        row_black.append("black")
        row_black.insert(0, fname.split(".")[0])
        writer.writerow(row_black)

    for fname1 in fname_white:
        haralick1 = np.load(os.path.join(path_haralick_white, fname1)).tolist()
        gray1 = np.load(os.path.join(path_gray_white, fname1)).tolist()
        edge1 = np.load(os.path.join(path_edge_white, fname1)).tolist()
        row_white = haralick1+gray1+edge1
        row_white.append("white")
        row_white.insert(0, fname1.split(".")[0])
        writer.writerow(row_white)

f.close()
