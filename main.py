# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 14:27:02 2023

@author: lexus
"""

import getDetectorMatrix
import lexus_utility as lexus
import matplotlib.pyplot as plot    

path = "D:/Python_prj/DIPLOM/spectrs_last/{}_Event.txt".format(0)
mass =  getDetectorMatrix.getDecetorMatrix(path)

lexus.fastPrint(mass[120][50:120])