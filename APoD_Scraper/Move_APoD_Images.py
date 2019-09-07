# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 15:09:27 2019

@author: wapisani

This script will get the sizes of images in a directory, and if the size is at least 1920x1080, will copy to the specified directory.
"""

# Import necessary libraries
import os
from PIL import Image

# Set source directory
source_directory = r"F:\Pictures\Space\APoD"

# Set destination directory
dest_directory = r"F:\Pictures\Wallpapers\1080p_or_higher\Space"

# Set the minimum width and height
min_width = 1980
min_height = 1080

# Storage array for images with size greater than
# or equal to the specified size
image_storage = []

print("Started walking through files...\nI will identify images with a resolution greater than or equal to {}x{}".format(min_width,min_height))

# Start walking through files
for root, directories, files in os.walk(source_directory):
    for f in files:
        if ".jpg" in f:
            
            # Open image
            im = Image.open(os.path.join(root,f))
            width, height = im.size
            
            # Check if the size of the image matches or exceeds the requirements
            if width >= min_width and height >= min_height:
                image_storage.append(f)
                im.close()

print("{} images found!".format(len(image_storage)))

# Start moving images to the destination directory
print("Now moving files to {}".format(dest_directory))

for i in image_storage:
    os.rename(os.path.join(source_directory,i),os.path.join(dest_directory,i))

print("Finished moving all {} images to {}".format(len(image_storage),dest_directory))