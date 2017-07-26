#!/usr/bin/python

from astropy.io import fits
import matplotlib.pyplot as plt

image = fits.open('../data/20170517_saturn/190ms/red/Saturnp19r_001.fit')

for name in image[0].header:
	print name + " = " + str(image[0].header[name])

data = image[0].data

# plt.imshow(data, cmap='Reds')
# plt.show()