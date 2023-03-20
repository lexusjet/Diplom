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
    
    
class Grid():
    def __init__(self, i, k):
        self.n = 0
        self.g = plot.GridSpec(i,k)
        self.fig = plot.figure()

            
        
    def addPlot(self, xValues, yValues, title):
        s = self.fig.add_subplot(self.g[(self.n*5):(self.n*5+3),0])
        s.plot(xValues, yValues)
        s.set_title(title)
        self.n +=1
        
    def show(self):
        plot.show()