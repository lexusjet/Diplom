# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 14:39:19 2023

@author: lexus
"""
import matplotlib.pyplot as plot

def fastPrint(arr):
    x = range(len(arr))
    graph = plot.plot(x, arr)
    plot.show()