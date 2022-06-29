# desciption
"""This code adds passwords for the key-based LSB method to the labels.
The generate_random_password() function comes from: 
https://geekflare.com/password-generator-python-code/"""

# import
import pandas as pd
import string
import random

# functions
def generate_random_password(char, length):
	random.shuffle(char)
	password = []
	for i in range(length):
		password.append(random.choice(char))

	random.shuffle(password)
	return "".join(password)


# path where labels are stored
path = "/media/cile/ADATA UFD/admin/labels"

# loading in data
data = pd.read_csv(f'{path}/1c-DB.csv')

# # passwords (weak/medium/hard), generated using https://my.norton.com/extspa/passwordmanager?path=pwd-gen
# passwords = ["WlVod", "nistO", "chuHa", "Trico", "5obromogiV", "wrUpLP4Pre", "t5puGaDoWl", "cr0sTo9idl", "F&-qA5O0*itHima", "gunl*A82+h!s8oS", "!R$SpOprOqos4ot", "ThEr3f5@aPreX!y"]

# defining key levels
easylen, easychar = 5, list(string.ascii_letters)
medlen, medchar = 10, list(string.ascii_letters + string.digits)
hardlen, hardchar = 15, list(string.ascii_letters + string.digits + "!@#$%^&*()")

# generating keys
amount_per_key = len(data[data["method"] == 2])//3 + 1
all_keys = []
for i in range(amount_per_key):
    all_keys.append(generate_random_password(easychar, easylen))
    all_keys.append(generate_random_password(medchar, medlen))
    all_keys.append(generate_random_password(hardchar, hardlen))

# randomly assign passwords to images
assigned_passwords = []
random_keys = random.sample(all_keys, len(data[data["method"] == 2]))
for name, row in data.iterrows():
    if row.method == 2:
        assigned_passwords.append(random_keys.pop())
    else:
        assigned_passwords.append("-")
data["key"] = assigned_passwords

# saving
data.to_csv(f'{path}/1d-DB.csv', index=False)