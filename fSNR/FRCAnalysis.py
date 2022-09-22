# -*- coding: utf-8 -*-
import numpy as np
import numpy.fft as ft
import matplotlib.pyplot as plt
from fSNR.Hamming import *
from Utils.DriftDetect import *
from fSNR.perform_FRC import *
from fSNR.meanFilter import *
from fSNR.findIntercept import *


def FRCAnalysis(imA, imB, pixelSize = 30.25, correctDrift = False, theta = 0, meanFilterwidth = 3):
    '''
    Performs FRC analysis on two images. If images are 3D, FRC is computed for each plane.

    Parameters
    ----------
    imA : 2D or 3D matrix containing photon counts of the first measurement
    imB : 2D or 3D matrix containing photon counts of the second measurement
    pixelsize : pixel size in nanometer {default: 30.25}
    driftCorrection : if do drift correction {default: false}
    meanFilterWidth : radius of the mean filter used to perform smooth the FRC curve {default：3}
    theta : if set, for each ring split the FRC analysis for pixels in the frequency domain for which -theta < angle < +theta
                          {default：0}
    Returns
    -------
    sSmallAngles, sLargeAngles, threeSigma, fiveSigma, smallAnglesResolution, LargeAnglesResolution

    '''
    checkArguments(imA, imB, theta)
    (w,h) = imA.shape
    hamming = Hamming(w,h)
    fftA = ft.fftshift(ft.fft2(imA*hamming))
    fftB = ft.fftshift(ft.fft2(imB*hamming))
    
    if correctDrift:
        #detect drift of imB
        drift, _ = DriftDetect(imA, imB, pixelSize)
        #correct drift
        fftB = fftShift(fftB, drift)
        print("applied drift correction of %f nm in x and and %f nm in y.\n" 
              % (drift[0] * pixelSize, drift[1] * pixelSize))
        
    smallAngles, largeAngles, threeSigma, fiveSigma = perform_FRC(fftA, fftB, h, w, theta)
    sSmallAngles = meanFilter(smallAngles, meanFilterwidth)
    sLargeAngles = meanFilter(largeAngles, meanFilterwidth)
    
    LargeAnglesResolution = np.ones([3,2]) * -1
    smallAnglesResolution = np.ones([3,2]) * -1
    fixedthreshold = np.ones(smallAngles.shape[0])/7.
    
    LargeAnglesResolution[0] = findIntercept(sLargeAngles, fixedthreshold, pixelSize)
    LargeAnglesResolution[1] = findIntercept(sLargeAngles, threeSigma, pixelSize)
    LargeAnglesResolution[2] = findIntercept(sLargeAngles, fiveSigma, pixelSize)
    
    smallAnglesResolution[0] = findIntercept(sSmallAngles, fixedthreshold, pixelSize)
    smallAnglesResolution[1] = findIntercept(sSmallAngles, threeSigma, pixelSize)
    smallAnglesResolution[2] = findIntercept(sSmallAngles, fiveSigma, pixelSize)
    
    
    return sSmallAngles, sLargeAngles, threeSigma, fiveSigma, smallAnglesResolution, LargeAnglesResolution


def checkArguments(imA, imB, theta):
    assert imA.shape == imB.shape, "images of unequal size"
    assert theta <= np.pi / 2 and theta >= 0,"invalid theta: theta < 0 or theta > pi / 2"


    
def fftShift(fftImage, shift):
    """multiply fft Image with complex exponential such that image is shifted by shift.
    
    Usage Warning: do not apply to raw ffts. Either apply Hamming Window or pad with zeros."""
    #this function needs some work to enable shifting a stacks of images.
    (w,h) = fftImage.shape
    x = np.arange(- np.floor( w/2), - np.floor(w/2) + w)
    y = np.arange(- np.floor( h/2), - np.floor(h/2) + h)
    [xF, yF] = np.meshgrid(x, y)
    
    return fftImage * np.exp(1j * 2 * np.pi * (shift[0] * xF / w + shift[1] * yF / h))