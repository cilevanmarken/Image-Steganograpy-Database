"""This code automizes the manipulations of images by steganographic methods, by generating all needed commands.
These commands can be copy pasted into the terminal in the corresponding tool directory. They can be found in 
the directory admin/"""

# import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read data
data = pd.read_csv('/media/cile/ADATA UFD/admin/labels/1d-DB.csv')

# initiate lists
LSBr, kLSB, LSBm, PVDc, BPCSc = [], [], [], [], []

# create commands
for name, row in data.iterrows():
    image_name=row.imageID[0:-4]
    path = f"/media/cile/ADATA UFD/data/raw/jpg/{row.phone}/{row.imageID}"
    png_path = f"/media/cile/ADATA UFD/data/raw/png/{row.phone}/{image_name}.png"
    dest_path = f'/media/cile/ADATA UFD/data/steg/{row.phone}/'
    png_dest_path = f'/media/cile/ADATA UFD/data/steg/{row.phone}/{image_name}.png'
    secret_path = f'/media/cile/ADATA UFD/code/2 - applying methods/messages/{row.message}'
    if row.method == 1:
        LSBr.append(f"python LSBRmain.py --path='{path}' --dest_path='{dest_path}' --encode --secret_path='{secret_path}' --image_name={image_name}")
    elif row.method == 2:
        kLSB.append(f"python kLSBmain.py --path='{path}' --dest_path='{dest_path}' --encode --secret_path='{secret_path}' --image_name={image_name} --key='{row.key}'")
    elif row.method == 3:
        LSBm.append(f"python LSBMmain.py --path='{path}' --dest_path='{dest_path}' --encode --secret_path='{secret_path}' --image_name={image_name}")
    elif row.method == 4:
        PVDc.append(f"python3 pvdEmbed.py '{secret_path}' '{png_path}' '{png_dest_path}'")
    elif row.method == 5:
        BPCSc.append(f"python -m bpcs.bpcs encode -i '{png_path}' -m '{secret_path}' -a 0.45 -o '{png_dest_path}'")
    
# store commands as one string
LSBr_commands = ""
for thing in LSBr:
    LSBr_commands += ";"
    LSBr_commands += thing

kLSB_commands = ""
for thing in kLSB:
    kLSB_commands += ";"
    kLSB_commands += thing

LSBm_commands = ""
for thing in LSBm:
    LSBm_commands += ";"
    LSBm_commands += thing

PVDc_commands = ""
for thing in PVDc:
    PVDc_commands += ";"
    PVDc_commands += thing

BPCSc_commands = ""
for thing in BPCSc:
    BPCSc_commands += ";"
    BPCSc_commands += thing

# write commands to text files
text_file = open("/media/cile/ADATA UFD/admin/commands/1_LSBr.txt", "w")
text_file.write(LSBr_commands[1:])
text_file.close()

text_file = open("/media/cile/ADATA UFD/admin/commands/2_kLSB.txt", "w")
text_file.write(kLSB_commands[1:])
text_file.close()

text_file = open("/media/cile/ADATA UFD/admin/commands/3_LSBm.txt", "w")
text_file.write(LSBm_commands[1:])
text_file.close()

text_file = open("/media/cile/ADATA UFD/admin/commands/4_PVD.txt", "w")
text_file.write(PVDc_commands[1:])
text_file.close()

text_file = open("/media/cile/ADATA UFD/admin/commands/5_BPCS.txt", "w")
text_file.write(BPCSc_commands[1:])
text_file.close()
