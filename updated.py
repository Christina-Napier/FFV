import binascii
import sys
import matplotlib
from pylab import *
from numpy import *
import numpy as np
sys.stdout=open("output.txt","w")

class fileInput()
def jpeg_to_decimal(jpeg_loc, as_rgb=True):
    '''
    Takes the location of a jpeg and returns it as a list of decimal values.
    :param jpeg_loc: The location of the Jpeg to read
    :param as_rgb: If True, returns rgb tuples.
    :return: A list of decimals representing the jpeg.
    '''
    with open(jpeg_loc, 'rb') as f:
        content = f.read()

    hex = binascii.b2a_hex(content)
    split_string_hex = map(''.join, zip(*[iter(hex)]*2))

    decimal_values = []
    for s in split_string_hex:
        dec = int(s, 16)
        decimal_values.append(dec)
        
    if as_rgb:
       
       t = zip(*[decimal_values[i::3] for i in range(3)])  # This branch gives an iterable
       print t
       #getting indentation errors with the below
    else:
	return decimal_values # This branch gives a list
jpeg_to_decimal(r'input.txt')
sys.stdout.close()

fileInput()

#Create test data with zero valued diagonal:
	#data = np.random.random_sample((512, 512))
	#data = What do I put in here to get the data from decimal_values??
	
	#rows, cols = np.indices((25,25))
	#data[np.diag(rows, k=0), np.diag(cols, k=0)] = 0

#Create new colormap, with white for zero 
#(can also take RGB values, like (255,255,255):
	#colors = [('white')] + [(cm.jet(i)) for i in xrange(1,256)]
	#new_map = matplotlib.colors.LinearSegmentedColormap.from_list('new_map', colors, N=256)

	#pcolor(data, cmap=new_map)
	#colorbar()
	#savefig('map2.png')
	#show()
