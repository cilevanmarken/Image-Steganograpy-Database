# description
"This code distributes the images over 10 groups (9 methods, 1 control). Complexity values have been distributed evenly"""

# import packages
import pandas as pd
import numpy as np

# path where labels are stored
path = "/media/cile/ADATA UFD/admin/labels"

# open data
data = pd.read_csv(f'{path}/1a-DB.csv')
data = data[np.invert(data[["imageID", "phone"]].duplicated())]

# distribution of methodd
grouped = data.groupby("phone")
assignments = []

for name, phone in grouped:
    sorted = phone.sort_values(by = "complexity", ascending=True)
    split = np.array_split(sorted, len(sorted)//11)

    for i in split:
        shuffled = i.sample(frac=1)
        for j in range(11):
            print([shuffled["imageID"].iloc[[j]].values[0], shuffled["phone"].iloc[[j]].values[0], shuffled["phoneYear"].iloc[[j]].values[0], shuffled["resolution (MP)"].iloc[[j]].values[0], shuffled["complexity"].iloc[[j]].values[0], j])
            assignments.append([shuffled["imageID"].iloc[[j]].values[0], shuffled["phone"].iloc[[j]].values[0], shuffled["phoneYear"].iloc[[j]].values[0], shuffled["resolution (MP)"].iloc[[j]].values[0], shuffled["complexity"].iloc[[j]].values[0], j])

# saving
assignments = pd.DataFrame(assignments, columns=["imageID", "phone", "phoneYear", "resolution", "complexity", "method"])
assignments.to_csv(f'{path}/1b-DB.csv', index=False)
