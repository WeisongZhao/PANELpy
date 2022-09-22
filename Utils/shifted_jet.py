# -*- coding: utf-8 -*-
import numpy as np 
from matplotlib.colors import LinearSegmentedColormap


def shifted_jet():
    shiftedjet = np.zeros((256, 3), dtype = 'uint8')
    roll = 42
    shiftedjet[0:roll,2] = np.linspace(0,255,roll)
    
    shiftedjet[roll:2*roll,2] = 255 * np.ones((1,roll))
    shiftedjet[roll:2*roll,0] = np.linspace(0,255,roll)
    
    shiftedjet[2*roll:3*roll,0] = 255 * np.ones((1,roll))
    shiftedjet[2*roll:3*roll,2] = np.linspace(255,0,roll)
    
    shiftedjet[3*roll:4*roll,0] = 255 * np.ones((1,roll))
    shiftedjet[3*roll:4*roll,1] = np.linspace(0,255,roll)
    
    shiftedjet[4*roll:5*roll,1] = 255 * np.ones((1,roll))
    shiftedjet[4*roll:5*roll,0] = np.linspace(255,0,roll)
    shiftedjet[5*roll:6*roll,1] = 255 * np.ones((1,roll))
    shiftedjet[5*roll:6*roll,0] = np.linspace(0,255,roll)
    shiftedjet[5*roll:6*roll,2] = np.linspace(0,255,roll)
    
    shiftedjet[6*roll:256,0] = 255 * np.ones((1,4))
    shiftedjet[6*roll:256,1] = 255 * np.ones((1,4))
    shiftedjet[6*roll:256,2] = 255 * np.ones((1,4))

    return shiftedjet


def sjet_colorbar():
    sjet = shifted_jet()  
    colormap = list(np.array(sjet/255))
    sjet_map = LinearSegmentedColormap.from_list('sJet', colormap)
    return sjet_map
