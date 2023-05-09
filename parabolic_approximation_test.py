# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 21:21:54 2023
parabolic approximation test
@author: lexus
"""
import getDetectorMatrix
import lexus_utility as lexus
import MonochoramtorLogClass as mlc
import Methods as methods

import matplotlib.pyplot as plt  
import numpy as np
from functools import reduce
from mpl_toolkits.mplot3d import Axes3D
import os.path

import seaborn as sb
from statistics import mean
    

path ="spectrs_2"
spectreFileName = "25_Event.txt"
logFileName = "Log_2.txt"
pathFileName = os.path.join(path, spectreFileName)

start = 0
end = 256

mass =  np.array(getDetectorMatrix.getDetectorMatrix(pathFileName))
mass = mass[:256, start:end]


log = mlc.MonochoramtorLog()
log.port("D:/Python_prj/DIPLOM/Diplom/spectrs_2/log_2.txt")
log.serialiseToJson("D:/Python_prj/DIPLOM/Diplom/spectrs_2/log_2.json")

mass= getDetectorMatrix.spectrumPreparation(mass[:256,:256])
plt.plot(range(len(mass)), mass)




 
    
