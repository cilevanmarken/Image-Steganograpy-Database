# description
"This code distributes labels of varying BPP over the images. Complexity has been taken into account"""

# import packages
import pandas as pd
import numpy as np

# path where labels are stored
path = "/media/cile/ADATA UFD/admin/labels"

# loading data
data = pd.read_csv(f'{path}/1b-DB.csv')

# defining embedding rates
bpp = [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1]

# distributing embedding rates randomly over images
bpp_dist = []
grouped = data.groupby(["phone", "method"])

for name, data in grouped:
    shuffled = data.sample(frac=1)
    split = np.array_split(shuffled, 7)
    for i in range(len(split)):
        for name, row in split[i].iterrows():
            if row["method"] == 0:
                bpp_dist.append([row["imageID"], row["phone"], row["phoneYear"], row["resolution"], row["complexity"], row["method"], 0])
            else:
                print([row["imageID"], row["phone"], row["phoneYear"], row["resolution"], row["complexity"], row["method"], bpp[i]])
                bpp_dist.append([row["imageID"], row["phone"], row["phoneYear"], row["resolution"], row["complexity"], row["method"], bpp[i]])

bpp_dist = pd.DataFrame(bpp_dist, columns = ["imageID", "phone", "phoneYear", "resolution", "complexity", "method", "embeddingRate"])

# add correpsonding labels for steganography and secret messages
text = []
steg = []

for name, row in bpp_dist.iterrows():
    if row["method"] == 0:
        text.append("-")
        steg.append(0)
    else:
        text.append(f"{str(row.embeddingRate/10)[2:]}_{row.resolution}.txt")
        steg.append(1)

bpp_dist["message"] = text
bpp_dist["stego"] = steg
bpp_dist.reset_index()

# saving
bpp_dist = bpp_dist[['imageID', "phone", "phoneYear", "resolution", "complexity", "stego", "method", "embeddingRate", "message"]]
bpp_dist.to_csv(f'{path}/1c-DB.csv', index=False)