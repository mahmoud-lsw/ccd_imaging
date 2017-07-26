import os
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
#import skimage.io as io  #thought it was a way to plot a "true color image" but is just another way of doing what matplotlib does

#### INCLUDE CONTROL HERE TO SEARCH AND ITERATE THROUGH COLORS

###########################################################################################################
###############################################DARKS#######################################################
###########################################################################################################

#### temporarily hardcoded
#import fits files as hdulist and convert into numpy arays
filepath = '../data/20170613_venus/3ms/darks/'
#filepath = '../data/20170613_saturn/19ms/darks/'

darks = {}
file_num = 0
for filename in os.listdir(filepath):
    if filename.endswith(".fit"): 
        print 'found image at ' + filepath + filename
        darks[file_num] = fits.open(filepath+filename)[0].data
        file_num+=1
    else:
    	print filename + ' is not a valid image file'

#establishing a loop that equals the number of images being used
loop_number = file_num - 1
#print(loop_number)

#view the numpy arrays as an images
#x=0
#for x in range(loop_number):
#	plt.imshow(darks[x], cmap='Greys')
#	plt.colorbar()
#	plt.show()

#stack dark image numpy arrays 
darks_stack = []
x = 0
for x in range(loop_number):
	darks_stack.append(darks[x])

#median combine all dark images into a final image
final_darks = np.median(darks_stack, axis=0)

#display final median combined numpy array
#plt.imshow(final_darks)
#plt.colorbar()
#plt.show()
#print(stop)

###########################################################################################################
###########################################################################################################
###########################################################################################################

###########################################################################################################
##############################################VISIBLE######################################################
###########################################################################################################

#### temporarily hardcoded
#import fits files as hdulist and convert into numpy arays
filepath = '../data/20170613_venus/3ms/visible/'
#filepath = '../data/20170613_saturn/19ms/visible/'

visible_image = {}
file_num = 0
for filename in os.listdir(filepath):
    if filename.endswith(".fit"): 
        print 'found image at ' + filepath + filename
        visible_image[file_num] = fits.open(filepath+filename)[0].data
        file_num+=1
    else:
    	print filename + ' is not a valid image file'

#establishing a loop that equals the number of images being used
loop_number = file_num - 1
#print(loop_number)

#subtract darks from numpy arrays and view images
x=0
for x in range(loop_number):
	visible_image[x] = (visible_image[x] - final_darks)
	plt.imshow(visible_image[x], cmap='Greys')
	plt.colorbar()
	plt.show()

#test to find the dimensions of the image
#image_size = red_image[0].shape
#print image_size #1024 high x 1360 wide

#Squishes each image into a 1D column array and finds where the max value is (vertical)
indexcolumnarray = []
x = 0
for x in range(loop_number):
	visible_column = []
	for i in range(1024):
		y=0
		for j in range(1360):
			y += visible_image[x][i][j]
		visible_column.append(y)
	index = np.where(visible_column == np.max(visible_column))
	indexcolumnarray.append(index[0][0])
print(indexcolumnarray)
#print(indexcolumnarray[0])

#Squishes each image into a 1D row array and finds where the max value is (horizontal)
indexrowarray = []
x = 0
for x in range(loop_number):
	visible_row = []
	for i in range(1360):
		y=0
		for j in range(1024):
			y += visible_image[x][j][i]
		visible_row.append(y)
	index = np.where(visible_row == np.max(visible_row))
	indexrowarray.append(index[0][0])
print(indexrowarray)
#print(indexrowarray[0])

#shift images vertically
visible_vertical_shifted = []
x = 0
for x in range(loop_number):
	visible_image[x] = np.roll(visible_image[x], (indexcolumnarray[0] - indexcolumnarray[x]), axis=0)
	visible_vertical_shifted.append(visible_image[x])

#shift images horizontally
visible_final_shifted = []
x = 0
for x in range(loop_number):
	visible_vertical_shifted[x] = np.roll(visible_vertical_shifted[x], (indexrowarray[0] - indexrowarray[x]), axis=1)
	visible_final_shifted.append(visible_vertical_shifted[x])

#median combine all shifted images into a final image
final_visible_image = np.median(visible_final_shifted, axis=0)

#display final median combined numpy array
plt.imshow(final_visible_image, cmap='Greys')
plt.colorbar()
plt.show()

#display final median combined numpy array
plt.imshow(final_visible_image)
plt.colorbar()
plt.show()

###########################################################################################################
###########################################################################################################
###########################################################################################################