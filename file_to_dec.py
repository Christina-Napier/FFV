import binascii
import sys
import matplotlib
from pylab import *
import numpy as np

sys.stdout = open("output.txt", "w")


def file_input(jpeg_loc, as_rgb=True):
    '''
    Takes the location of a jpeg and returns it as a list of decimal values.
    :param jpeg_loc: The location of the Jpeg to read
    :param as_rgb: If True, returns rgb tuples.
    :return: A list of decimals representing the jpeg.
    '''
    with open(jpeg_loc, 'rb') as f:
        content = f.read()

    hex = binascii.b2a_hex(content)
    split_string_hex = map(''.join, zip(*[iter(hex)] * 2))

    data = []
    for s in split_string_hex:
        dec = int(s, 16)
        data.append(dec)

    if as_rgb:

        t = zip(*[data[i::3] for i in range(3)])  # This branch gives an iterable
        print t
        # getting indentation errors with the below
    else:
        return data  # This branch gives a list




file_input(r'C:\Users\LAB\PycharmProjects\untitled2\py\input.txt')
sys.stdout.close()
