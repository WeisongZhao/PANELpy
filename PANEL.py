# -*- coding: utf-8 -*-

import numpy as np
from fSNR.fSNRmap import fSNRmap
from Utils.otsu import *
import datetime


def PANEL(stack, pixelsize = 30.25, backgroundIntensity = 5, skip = 1, blockSize = 64, \
          driftCorrection = False, amedianfilter = True, EnableOtsu = True):
    '''
    PANEL is a filtered rFRC map, for biologists to qualitatively pinpoint regions with low reliability as a concise visualization

    Parameters
    ----------
    stack : input two images to be evaluated, ndarray, shape (2, M, N).
    pixelsize : pixel size in nanometer {default: 30.25}
    backgroundIntensity :  background intensity (0~255 range, 8bit) {default: 5}
    skip : skip size to accelerate the rFRC calculation {default: 1}
    blockSize : rFRC block size {default: 64}
    driftCorrection : if do drift correction {default: false}
    amedianfilter : whether do adaptive filter after rFRC mapping {default: true}
    EnableOtsu : whether enable otsu filter in PANEL merging {default: true}

    Returns
    -------
    PANEL_result : PANEL_result = [rFRCmap, PANELs, absolute_value]
                   absolute_value : [minimum resolution, maximum resolution, mean resolution, rFRC value]

    '''
    print('PANEL estimation start...')
    start_time = datetime.datetime.now()
    print('High-resolution fSNR estimation...')
    rFRCmap = fSNRmap(stack, pixelsize, backgroundIntensity, skip, blockSize, driftCorrection, amedianfilter)
    PANELs = otsu(rFRCmap, EnableOtsu)
    absolute_value = caculate_global(rFRCmap)
    print('PANEL estimation done, thank you for your waiting')
    elapsed_time = datetime.datetime.now() - start_time
    print('Total time cost: %s' %elapsed_time)
    PANEL_result = [rFRCmap, PANELs, absolute_value]
    return PANEL_result


def caculate_global(rFRCmap):
    '''
    Caculate the rFRCmap's global metric

    Parameters
    ----------
    rFRCmap 

    Returns
    -------
    absolute_value : [minimum resolution, maximum resolution, mean resolution, rFRC value]

    '''
    [w, h] = rFRCmap.shape
    non_zero_sum = np.array(0, dtype = 'float32')
    FV_sum = np.array(0, dtype = 'float32')
    for x in range(w):
        for y in range(h):
            FV = rFRCmap[x, y]
            if FV !=0:
                max_FV = np.array((rFRCmap[x, y]), dtype = 'float32')
                min_FV = np.array((rFRCmap[x, y]), dtype = 'float32')
    for xx in range(w):
        for yy in range(h):
            FV = rFRCmap[xx, yy]
            if FV > 0:
                non_zero_sum = non_zero_sum + 1
                FV_sum = FV_sum + FV
                if FV > max_FV:
                    max_FV = FV
                elif FV < min_FV:
                    min_FV = FV
    resolution = float(FV_sum / non_zero_sum)
    rFRC = float(FV_sum / (non_zero_sum * min_FV)) - 1
    print('Global metrics:\n')
    print('rFRC value:',rFRC , '\n')
    print('mean resolution:',resolution , 'nm\n')
    print('minimum resolution:',min_FV , 'nm\n')
    print('maximum resolution:',max_FV , 'nm\n')
    absolute_value = np.array((min_FV, max_FV, resolution, rFRC), dtype = 'float32')
    return absolute_value
                


    
    
    