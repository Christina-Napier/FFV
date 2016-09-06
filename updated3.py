import binascii
import sys
import matplotlib
from pylab import *
from numpy import *
import numpy as np
#sys.stdout=open("output.txt","w")
rgb_values=''

def hex_RGB(minimum, maximum, value):
    minimum, maximum = float(minimum), float(maximum)
    ratio = 2 * (value-minimum) / (maximum - minimum)
    b = int(max(0, 255*(1 - ratio)))
    r = int(max(0, 255*(ratio - 1)))
    g = 255 - b - r
    return r, g, b

def text_to_decimal(txt_loc):
    global rgb_values
    '''
    Takes the location of a text file and returns it as a list of decimal values.
    param jpeg_loc: The location of the Jpeg to read
    :param as_rgb: If True, returns rgb tuples.
    :return: A list of decimals representing the jpeg.
    '''
    with open(txt_loc, 'rb') as f:
        content = f.read()

    hex = binascii.b2a_hex(content)
    
    split_string_hex = ''.join(str(v) for v in hex)

    decimal_values = []
    counter=1
    for s in split_string_hex:
        dec = int(s, 16)
        decimal_values.append(hex_RGB(1,9,dec))
    rgb_values = decimal_values


def decimal_to_jpeg():

    rows, cols = np.indices((25,25))

    #Create new colormap, with white for zero 
    #(can also take RGB values, like (255,255,255):
    colors = [('white')] + [(cm.jet(i)) for i in range(1,256)]
    new_map = matplotlib.colors.LinearSegmentedColormap.from_list('new_map', colors, N=256)

    pcolor(rgb_values, cmap=new_map)
    colorbar()
    savefig('map2.png')
    show()
    
text_to_decimal(r'input.txt')
decimal_to_jpeg()
print ('done')

#sys.stdout.close()




