# -*- coding: utf-8 -*-
# computes Hamming function

import numpy as np

def Hamming(w,h):
    alpha = 0.54
    beta = 1-alpha
    xv = alpha - beta * np.cos(2*np.pi / (w-1) * np.arange(w))
    yv = alpha - beta * np.cos(2*np.pi / (h-1) * np.arange(h))
    hamming = np.zeros([w,h])
    for i in range(h):
        hamming[i] = xv * yv[i]
    return hamming