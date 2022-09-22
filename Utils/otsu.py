# -*- coding: utf-8 -*-
from skimage import filters
import numpy as np

def otsu(rFRCmap, EnableOtsu = True):
    [width, height] = rFRCmap.shape
    inter = np.zeros((width, height), dtype = 'uint8')
    inter[:, :] = rFRCmap[:, :]
    rFRCmap_new = np.zeros((width, height), dtype = 'uint8')
    rFRCmap_new[:, :] = rFRCmap[:, :]
    maxfrc = np.max(inter)
    inter[inter == 0] = maxfrc
    minfrc = np.min(inter)  
    rFRCmap_new[rFRCmap_new >= minfrc] == (rFRCmap_new/minfrc) - 1
    rFRCmap_new[rFRCmap_new > 1] = 1
    rFRCmap_new[rFRCmap_new < 0] = 0
    if EnableOtsu:
        rFRCmap_new = rFRCmap_new - 0.4
        rFRCmap_new[rFRCmap_new < 0] = 0
        thresh = filters.threshold_otsu(inter/255)
        rFRCmap_new[rFRCmap_new > 1] = 1
        rFRCmap_new[rFRCmap_new < thresh*(np.max(rFRCmap_new))] = 0
    return rFRCmap_new
 
    