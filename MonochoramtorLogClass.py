# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 17:52:36 2023

@author: lexus
"""
import re as regexp

class MonochoramtorLog():
    def __init__(self, pathToLog):
        file = open(pathToLog, 'r')
        data = file.read()
        regexp1 = regexp.findall(r"(date|start|stop|step)=([^>;]*)", data)
        self.date = regexp1[0][1]
        self.angleStart = float(regexp1[1][1])
        self.angleStop = float(regexp1[2][1])
        self.angleStep = float(regexp1[3][1])
        self.engineStart = int(regexp1[4][1])
        self.engineStop = int(regexp1[5][1])
        self.engineStep = int(regexp1[6][1])
        file.close()
    
        