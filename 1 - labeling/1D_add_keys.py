# desciption
"""This code adds passwords for the key-based LSB method to the labels"""

# import
import pandas as pd
import random

# path where labels are stored
path = "/media/cile/ADATA UFD/admin/labels"

# loading in data
data = pd.read_csv(f'{path}/1c-DB.csv')

# passwords (weak/medium/hard), generated using https://my.norton.com/extspa/passwordmanager?path=pwd-gen
passwords = ["WlVod", "nistO", "chuHa", "Trico", "5obromogiV", "wrUpLP4Pre", "t5puGaDoWl", "cr0sTo9idl", "F&-qA5O0*itHima", "gunl*A82+h!s8oS", "!R$SpOprOqos4ot", "ThEr3f5@aPreX!y"]

# randomly assign passwords to images
assigned_passwords = []
randomized_passwords = random.sample(84 * passwords, len(84 * passwords))[:-2]
for name, row in data.iterrows():
    if row.method == 2:
        assigned_passwords.append(randomized_passwords.pop())
    else:
        assigned_passwords.append("-")
data["key"] = assigned_passwords


# saving
data.to_csv(f'{path}/1d-DB.csv', index=False)