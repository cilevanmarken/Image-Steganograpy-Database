"""This code converts jpg to png, which is needed for the PCS and PVD method"""

# importing
from PIL import Image
import os

# list of phones
phones = os.listdir("D:\data\\raw\jpg")

# list of jpg's
steg = []
for image in os.listdir(f"D:\data\\raw\png\HUAWEI EML-L09 - NOHDR\\"):
    steg.append(image[0:-4])

# converting to png
for phone in phones:
    for image in os.listdir(f"D:\data\\raw\jpg\{phone}\\"):
        image_name = image[0:-4]
        if image_name not in steg:           
            path = f"D:\data\\raw\jpg\{phone}\{image}"
            dest_path = f"D:\data\\raw\png\{phone}\{image_name}.png"           
            im1 = Image.open(path)
            im1.save(dest_path)
