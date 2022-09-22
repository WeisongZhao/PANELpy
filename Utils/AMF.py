# -*- coding: utf-8 -*-
import numpy as np


def AMF(rFRC_array):
    [width, height] = rFRC_array.shape
    window_size = 3
    threshold = float(2)
    rFRC_array_copy = np.array(rFRC_array, dtype = 'float32')
    new_array = np.array(rFRC_array_copy, dtype = 'float32')
    temp = np.zeros((window_size*window_size), np.float32)
    win = np.int((3-1) / 2)
    for x in range(win, width - win):
        for y in range(win, height - win):
            flage = 0 
            for i in range(-win, win + 1, 1):
                for j in range(-win, win + 1, 1):
                    temp[flage] = rFRC_array_copy[x+i, y+j]
                    flage = flage + 1
            temp.sort()
            if (threshold * temp[np.int((flage) / 2)] < rFRC_array_copy[x, y]):
                new_array[x, y] = temp[np.int(flage / 2)]
    return new_array
    