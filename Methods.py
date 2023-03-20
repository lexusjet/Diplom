# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 20:21:37 2023

@author: lexus
"""
from functools import reduce
import numpy as np

def linreg(X, Y):
    """
    return a,b in solution to y = ax + b such that root mean square distance between trend line and original points is minimized
    """
    N = len(X)
    Sx = Sy = Sxx = Syy = Sxy = 0.0
    for x, y in zip(X, Y):
        Sx = Sx + x
        Sy = Sy + y
        Sxx = Sxx + x*x
        Syy = Syy + y*y
        Sxy = Sxy + x*y
    det = Sxx * N - Sx * Sx
    return (Sxy * N - Sy * Sx)/det, (Sxx * Sy - Sx * Sxy)/det


def method(mass):
    array = np.sum(mass, 0)
    array = array.dot(1/len(mass))
    anser = []
    
    xValues = range(0,3)
    for i in range(len(array)-3):
        anser.append(linreg(xValues, array[i:i+3]))
    
    return  list(map(lambda x: x[0], anser))



def IntegralMethod(mass):
    anser = []
    anser = np.sum(mass, 0)
    anser = np.sum(anser)

    return anser
    
