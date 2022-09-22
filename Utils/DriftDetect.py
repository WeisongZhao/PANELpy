# -*- coding: utf-8 -*-
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def DriftDetect(imA, imB, pixelSize, p0 = (-1, -1, -1, -1, -1, -1, -1), verbose = False, fitWindow =10):
    """Detect drift between imA and imB. 
     Programm uses autocorrelation and least squares fitting from scipy's curve_fit func.
     p0 is used as initial guess. autocorrelation landscape shows local minima when beads are used.
     Therefore, the initial guess must be accurate, especially the center position guess.
     If verbose is True, the autocorrelation, fitted gaussian center
     and zero shift center are plotted. Also the shift will be printed in nm.
     Returns: center, centersigma in number of pixels."""
    assert (imA.shape ==imB.shape and imA.shape[0]==imA.shape[1]), "images non-square or non-equal sized"
    imcenter = int(imA.shape[0]/2)

    
    #perform autocorrelation
    corr = np.fft.fftshift(np.fft.ifft2(np.fft.fft2(imA) * np.conj(np.fft.fft2(imB))))
    #take center region for Gaussian fitting
    corr = corr[imcenter - fitWindow : imcenter + fitWindow, imcenter - fitWindow : imcenter + fitWindow]
    
    # Create x and y indices
    x = np.arange(corr.shape[0])
    y = np.arange(corr.shape[0])
    coord = np.meshgrid(x, y)
    
    #if parameter guess is unset, make intelligent estimate.
    if p0[0] == -1:
        p0 = (np.max(abs(corr)), fitWindow, fitWindow, 1, 1, 0, 0)
    
    
    #perform 2D gauss fit
    popt, pcov = curve_fit(twoD_Gaussian, coord, abs(corr).ravel(), p0=p0)
    
    #take relevant parameters
    drift = popt[1:3] - [fitWindow, fitWindow]
    driftSigma = np.sqrt([pcov[1,1], pcov[2,2]])
    
    #plt and print
    if verbose:
        plt.imshow(abs(corr))
        plt.plot([0,fitWindow*2],[fitWindow,fitWindow], 'r', linewidth = 0.5)
        plt.plot([fitWindow, fitWindow], [0, fitWindow * 2], 'r', linewidth = 0.5)
        plt.colorbar()
        plt.scatter(popt[1], popt[2], s=10)
        plt.show()
        
        print ("using initial parameters (Amplitude, xpos, ypos, xsigma, ysigma, theta, background) equal to " + str(p0))

        print (u"shift in x is  {:.3f} \u00B1 {:.3f}  pixels\n".format(drift[0], driftSigma[0])
               + u"shift in y is  {:.3f} \u00B1 {:.3f} pixels\n".format(drift[1], driftSigma[1]) 
               + u"total shift is {:.3f} \u00B1 {:.3f} nm for pixel size of {:d} nm \n".format(
                   np.linalg.norm(drift-[fitWindow, fitWindow])*pixelSize,
                   np.linalg.norm(driftSigma*pixelSize),
                   pixelSize
               ) 
              )
    return drift, driftSigma

def twoD_Gaussian(coord, amplitude, xo, yo, sigma_x, sigma_y, theta, offset):
    x = coord[0]
    y = coord[1]
    xo = float(xo)
    yo = float(yo)    
    a = (np.cos(theta)**2)/(2*sigma_x**2) + (np.sin(theta)**2)/(2*sigma_y**2)
    b = -(np.sin(2*theta))/(4*sigma_x**2) + (np.sin(2*theta))/(4*sigma_y**2)
    c = (np.sin(theta)**2)/(2*sigma_x**2) + (np.cos(theta)**2)/(2*sigma_y**2)
    g = offset + amplitude*np.exp( - (a*((x-xo)**2) + 2*b*(x-xo)*(y-yo) 
                            + c*((y-yo)**2)))
    return g.ravel()