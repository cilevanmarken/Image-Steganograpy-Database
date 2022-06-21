# Creating an Image-Steganograpy-Database
This repository contains all code needed for creating an image steganography database in the spatial domain, as part of a Bachelor Thesis. Methods used are LSB replacement, key-based LSB replacement, LSB matching, PVD and BPCS.

# Images
The first thing needed for an image steganography database in the spatial domain is images. These images shouldn't contain any steganography and are thus taken manually using multiple camera's. The images are ordered in multiple folders, where every folder corresponds to one camera. 

# Labeling
These images have been labeled using the following code (code > 1 - labeling):
1. 1A_add_labels.py: creates a csv with per image, the camera used to take the image, manufacturing year of the phone and the resolution and complexity of the image.
2. 1B_add_methods.py: distributes methods over the images, taken into account the complexities of the images.
3. 1C_add_bpp.py: adds embedding rates and corresponding messages.
4. 1D_add_keys: adds passwords for key-based LSB

Now all images are labeled in one csv file.

# Applying methods
Five steganographic methods in the spatial domain have been used. For every one of these methods, external code was used. These tools can be found in code > 2 - applying methods. 
