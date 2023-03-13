# -*- coding: utf-8 -*-
import numpy as np

def getDetectorMatrix(fileName):
    file = open(fileName)
    matrix = np.loadtxt(file)
    file.close()
    return matrix

