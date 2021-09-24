from datetime import datetime
from os import listdir
from random import randint

import cv2 as cv
import numpy as py
import pyautogui as pg

# This is following tutorial #2 of https://www.youtube.com/watch?v=wlYPhdTbRmk
# 00:00 | Intro
# 01:45 | Image Representation
# 04:02 | Values that Represent our Pixels
# 07:20 | Accessing Pixel Values
# 08:45 | Changing Pixel Colors
# 11:37 | Copying & Pasting Parts of Image
# 15:07 | Outro


# print out the img being read as a numpy array using the print function
img_webp = cv.imread('images/python_logo.webp', -1)
img_cloud = cv.imread('images/cloud_strife.jpg', -1)

print('Getting images returned as a numpy array')
print(img_webp)
print(img_cloud)


# With the img now read and assigned to a variable we can use the method
# .shape to find number of: rows, columns and channels.
# It is returns as a tuple:
# (rows, columns, color space (RGB will be converted to BGR)) 
# (height, width, color channels)
# (h, w, c)
print('Getting shape of img')
print(img_cloud.shape)  # This will print(32, 27, 3)

# Side Note: when getting the shape the numpy array will be formatted
# as followed for a 2x2 img:
# Structure is as follows:
# Outer array is the image.
# First internal array is the row.
# The innermost array is the column.
# [image[row[column], [column], [column]]]
# Example of a 2x2 img being returned as a numpy array:
# [
# [[0, 0, 0], [255, 255, 255]],     => row 0, columns 0, 1
# [[0, 0, 0], [125, 0, 255]]        => row 1, columns 0, 1
# ]


# Accessing pixels in the image
print('Accessing pixels: 9th row.')
print(img_cloud[10])  # width-1 of image is your max
print(
'''Access pixels: 9th row, 10th column''' 
)
print(img_cloud[10][11])  # height-1 of image is your max
print(
'''Accessing pixels: 9th row, 2nd to 4th column''')
print(img_cloud[10][2:5])  # You can slice arrays to return only what is wanted

# Using whats been done we can actually alter the pixel values
# of the image. For this example we use a for loop.
for i in range(500):  # Go through img up to 500th row.
    for j in range(img_cloud.shape[1]):  # Go through all columns per i .
        img_cloud[i][j] = [randint(0, 255), randint(0, 255), randint(0, 255)]

cv.imshow('IMAGE', img_cloud)  # To display the altered image.
cv.waitKey(0)  # Waits an infinite amount of time.
cv.imwrite('screwed_up.jpg', img_cloud)  # To save your altered image.
cv.destroyAllWindows()  # Destroys all imshow windows.


# We can copy a section of the image and paste into onto another part 
# of the image without losing the copied section.
# Following this structure:
# variable = variableWithImage[row start:row end, column start:column end]
# Copy all pixels in 300th to 600th row
# Copy all pixels in 200th to 400th row
copied = img_cloud[300:600, 200:400]  # row diff 300, col diff 200
# When copying its required: copied dimensions identical to pasted dimensions
img_cloud[400:700, 800:1000] = copied  # row diff 300, col diff 200


# Messing around with randint
sr, er, sc, ec = randint(0, 500), \
                 randint(501, 1000), \
                 randint(300, 800), \
                 randint(801, 1050)
copied = img_cloud[sr:er, sc:ec]

diff_r = er - sr
diff_c = ec - sc
sr, sc = randint(0, 150), randint(1, 500)
er, ec = sr + diff_r, sc + diff_c
img_cloud[sr:er, sc:ec] = copied

cv.imshow('IMAGE', img_cloud)  # To display the altered image.
cv.waitKey(0)  # Waits an infinite amount of time.
cv.imwrite('screwed_up.jpg', img_cloud)  # To save your altered image.
cv.destroyAllWindows()  # Destroys all imshow windows.

