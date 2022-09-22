# -*- coding: utf-8 -*-

import numpy as np
from sys import float_info

def perform_FRC(fftA, fftB, h, w, theta):
    '''
    Calculates FRC curve; 3Sigma and 5Sigma curves
    '''
    #int cast floors values
    xc = int(w / 2)
    yc = int(h / 2)
    rMax = min(w - xc, h - yc)
    #init return values
    smallAngles = np.zeros(rMax)
    largeAngles = np.zeros(rMax)
    threeSigma = np.zeros(rMax)
    fiveSigma = np.zeros (rMax)
    
    #init local vars
    corr_largeAngles = np.zeros(rMax, dtype = 'complex128')
    absA_largeAngles = np.zeros(rMax)
    absB_largeAngles = np.zeros(rMax)
    corr_smallAngles = np.zeros(rMax, dtype = 'complex128')
    absA_smallAngles = np.zeros(rMax)
    absB_smallAngles = np.zeros(rMax)
    
    #loop over all pixels and update local vars
    for x in range(w):
        for y in range(h):
            #r is the ring number that the pixel is in
            r =  int(round(np.sqrt((x-xc)**2+(y-yc)**2)))
            #we include only full rings in the image, no truncated rings
            if (r < rMax):
                threeSigma[r] += 1
                fiveSigma[r] += 1
               # print("value of theta is %f" %theta)
             #   print("angle of data point equals: %f" % np.arctan(abs(y-yc)/ (abs(x - xc) + float_info.epsilon)))
                if (theta == 0 or np.arctan(abs(y-yc)/ (abs(x - xc) + float_info.epsilon)) > theta ):
                    corr_largeAngles[r] += fftA[y, x] * np.conj(fftB[y, x])
                    absA_largeAngles[r] += abs(fftA[y,x]**2)
                    absB_largeAngles[r] += abs(fftB[y,x]**2)
                else:
                    corr_smallAngles[r] += fftA[y, x] * np.conj(fftB[y, x])
                    absA_smallAngles[r] += abs(fftA[y,x]**2)
                    absB_smallAngles[r] += abs(fftB[y,x]**2)
    
    #compute class vars
    largeAngles = abs(corr_largeAngles) / np.sqrt(absA_largeAngles*absB_largeAngles + float_info.epsilon)
    smallAngles = abs(corr_smallAngles) / np.sqrt(absA_smallAngles*absB_smallAngles + float_info.epsilon)
    threeSigma = 3 / np.sqrt(threeSigma / 2)
    fiveSigma = 5 / np.sqrt(fiveSigma / 2)
    
    #set values higher than 1 to 1.
    for i in range(rMax):
        if (threeSigma[i] > 1):
            threeSigma[i] = 1
        if (fiveSigma[i] > 1):
            fiveSigma[i] = 1

    return smallAngles, largeAngles, threeSigma, fiveSigma