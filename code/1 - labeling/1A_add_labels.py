# description
"""This code labels the images. It adds the complexity of the image and information regarding camera and resolution"""

# importing packages
import os
import pandas as pd
import numpy as np
from skimage.io import imread
from scipy import ndimage
from skimage import io, color
import cv2

# path where images are stored per camera
path = "/media/cile/ADATA UFD/data"

# functions: compute complexity of an image
def complexity(image, phone):
    img = cv2.imread(f"{path}/{phone}/{image}")
    lab_img = cv2.cvtColor(img, cv2.COLOR_RGB2LAB)

    M = lab_img.shape[0]
    N = lab_img.shape[1]

    ksize = -1
    gX = cv2.Sobel(lab_img, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=ksize)
    gY = cv2.Sobel(lab_img, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=ksize)
    gX = cv2.convertScaleAbs(gX)
    gY = cv2.convertScaleAbs(gY)

    combined = abs(cv2.addWeighted(gX, 0.5, gY, 0.5, 0))
    X, Y, Z = combined.shape
    reshaped = combined.reshape((X * Y, Z))

    total_sum = np.sum(np.max(reshaped, axis = 1))
    complexity = (1/(N*M))*total_sum

    return complexity

# creating a pandas dataframe
images_list = []
phone_list = []

for phone in os.listdir(f"{path}/"):
    for image in [x for x in os.listdir(f"{path}/{phone}/")]:
        if phone == "APPLE Ipod touch - NOHDR":
            year = 2007
            resolution = 8
        elif phone == "ASUS Zenfone 8 - AUtoHDR":
            year = 2021
            resolution = 64
        elif phone == "HUAWEI EML-L09 - NOHDR":
            year = 2018
            resolution = 24
        elif phone == "ONEPLUS Nord CE 5G - NOHDR":
            year = 2021
            resolution = 64
        elif phone == "OPPO Find X3 Lite - HDR":
            year = 2021
            resolution = 64
        elif phone == "OPPO Find X3 Neo - AutoHDR - mist":
            year = 2021
            resolution = 50
        elif phone == "SAMSUNG Galaxy A32 - HDR":
            year = 2021
            resolution = 64
        elif phone == "SAMSUNG Xcover Pro - HDR":
            year = 2020
            resolution = 25
        elif phone == "SONY Xperia 1 III - NOHDR":
            year = 2021
            resolution = 12
        elif phone == "XIAOMI Mi 11i - HDR":
            year = 2021
            resolution = 108
        elif phone == "XIAOMI Poco F3 - HDR":
            year = 2021
            resolution = 48

        compl = complexity(image, phone)
        images_list.append([image, phone, year, resolution, compl])
        
# gathering all labels in a pandas DataFrame
labels = pd.DataFrame(images_list, columns = ['imageID', 'phone', 'phoneYear', 'resolution (MP)', 'complexity'])
labels.to_csv('admin/labels/1a-DB.csv', index=False)