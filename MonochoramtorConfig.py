# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 17:52:36 2023

@author: lexus
"""
import re as regexp
import os.path
import json

class MonochoramtorConfig():
    def __init__(self):
        self.date = None 
        self.angleStart = None 
        self.angleStop = None 
        self.angleStep = None 
        self.engineStart = None 
        self.engineStop = None 
        self.engineStep = None 
        
        
        
    def loadFromJson(self,pathToLog):
        file = open(pathToLog, 'r')
        data = json.load(file)
        self.date = data["date"]
        self.angleStart = float(data["angleStart"])
        self.angleStop = float(data["angleStop"])
        self.angleStep = float(data["angleStep"])
        self.engineStart = int(data["engineStart"])
        self.engineStop = int(data["engineStop"])
        self.engineStep = int(data["engineStep"])
        file.close()
        
    def serialiseToJson(self , path):
        file =  open(path, "w+")
        json.dump(self.__dict__,file)
    
        