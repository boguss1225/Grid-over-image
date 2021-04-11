import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image
import os
from os import listdir

print("-------------------------------------------")
print("------------   Grid Over Image  -----------")
print("-------------------------------------------")

#Set target folder path
print("Enter image folder path: ")
TARGET_PATH = input()

#Set Grid Interval Here
dx = int(input("Set Grid Interval dx: "))
dy = int(input("Set Grid Interval dy: "))
#dx, dy = 128,128

#Set dpi
dpi = 100

# make destin folder
DESTIN_PATH=TARGET_PATH+"/Grided_Images"
if not os.path.exists(DESTIN_PATH):
    os.makedirs(DESTIN_PATH)

#Load images from the TARGET_PATH
loaded_images = list()
for filename in listdir(TARGET_PATH):
    # load image
    if not(filename.startswith('.') or os.path.isdir(TARGET_PATH + '/' +filename)):
        img_data = plt.imread(TARGET_PATH + '/' +filename)
        # store loaded image
        loaded_images.append(img_data)

cnt=0
# Cover Grid
for img in loaded_images:
    img=img.copy()
    #set interval
    
    # set grid color 
    grid_color = [255,255,255]
    img[:,::dy,:] = grid_color
    img[::dx,:,:] = grid_color
    loaded_images[cnt] = img
    cnt=cnt+1
    #plt.imshow(img)
    #plt.show()

# Save grided image
cnt=0
for filename in listdir(TARGET_PATH):
    #save
    if not(filename.startswith('.') or os.path.isdir(TARGET_PATH + '/' +filename)):
        #set figure
        height, width, depth = loaded_images[cnt].shape
        print(depth)
        figsize = width / float(dpi), height / float(dpi)
        plt.figure(figsize=figsize)
        plt.imshow(loaded_images[cnt])
        plt.gca().set_axis_off()
        plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
        plt.margins(0,0)
        plt.gca().xaxis.set_major_locator(plt.NullLocator())
        plt.gca().yaxis.set_major_locator(plt.NullLocator())
        #save figure
        plt.savefig(DESTIN_PATH+"/"+filename , bbox_inches = 'tight', pad_inches = 0)
        cnt=cnt+1

print("<<<<<<<<<<<<<<<<<<<<<<<  ALL DONE!   >>>>>>>>>>>>>>>>>>>>>>>")

#/Users/bogus/Documents/1_STUDY/3_Projects/Grid-over-image/test_image



