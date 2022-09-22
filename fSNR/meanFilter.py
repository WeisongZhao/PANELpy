# -*- coding: utf-8 -*-
# Smooth data using a moving mean filter of (2 * mean_width +1) elements
import numpy as np

def meanFilter(data, width):
    d = data.shape[0]
    smoothData = np.zeros(d)
    for i in range(d):
        if ( i <= width ):
            smoothData[i] = np.mean(data[:i + width + 1])
        elif (i > width and i < d - width):
            smoothData[i] = np.mean(data[i - width : i + width + 1])
        elif ( i >= d - width):
            smoothData[i] = np.mean(data[i - width:])
        else:
            print("error found in meanFilter program")
    return smoothData