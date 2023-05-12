# -*- coding: utf-8 -*-
import numpy as np
from statistics import mean
                               
def spectrum_preparation(mass):
    mass = mass.transpose()
    dispersions = list(map(np.var, mass))
    sigmas = list(map(lambda x : pow(x, 0.5), dispersions))

    for i in range(len(mass)):
        j = 0
        mn = mean(mass[i])
        sigma = sigmas[i]
        while j < len(mass[i]):
            if(mass[i][j] > mn + sigma * 3 or mass[i][j] < mn - sigma * 3):
                mass = np.delete(mass, j, axis = 1)
            j += 1
    
    
    dispersions = list(map(np.var, mass))
    sigmas = list(map(lambda x : pow(x, 0.5), dispersions))
    mass = mass.transpose()
    
    return mass
