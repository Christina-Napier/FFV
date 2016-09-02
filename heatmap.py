"""Produce custom labelling for a colorbar.

Contributed by Scott Sinclair
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from .file import file_to_dec

def heatmap():
    # Create test data with zero valued diagonal:
    data = [(116, 101, 120), (116, 32, 116), (101, 120, 116), (32, 116, 101), (120, 116, 32), (116, 101, 120), (116, 32, 97), (115, 108, 100), (107, 104, 102), (115, 104, 100), (102, 107, 106), (104, 97, 115), (100, 107, 102), (108, 104, 97), (115, 100, 107), (102, 106, 104), (107, 115, 97), (106, 100, 102), (107, 104, 106), (115, 108, 107), (106, 115, 100)]
    #data = np.random.random_sample((512, 512))#
    #data = What do I put in here to get the data from decimal_values??

    rows, cols = np.indices((25,25))
    data[np.diag(rows, k=0), np.diag(cols, k=0)] = 0

    # Create new colormap, with white for zero
    # (can also take RGB values, like (255,255,255):
    colors = [('white')] + [(cm.jet(i)) for i in xrange(1,256)]
    new_map = matplotlib.colors.LinearSegmentedColormap.from_list('new_map', colors, N=256)

    plt.pcolor(data, cmap=new_map)
    plt.colorbar()
    plt.savefig('map2.png')
    plt.show()
