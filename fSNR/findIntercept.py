# -*- coding: utf-8 -*-

def findIntercept(data, threshold, pixelSize):
    '''Calculates the first intercept abscissa between data (non strictly decraising) and a given threshold curve.'''
    assert( data.shape == threshold.shape), 'data and threshold of unequal length'
    d = data.shape[0]
    intercept = -1
    resolution = -1
    for i in range(3,d-1):
        if (data[i] < threshold[i] and max(data[i-1], data [i-2], data[i-3]) > threshold[i]):
            resolution = 2 * d * pixelSize / (i)
            intercept = i + 1
            break
    return resolution, intercept