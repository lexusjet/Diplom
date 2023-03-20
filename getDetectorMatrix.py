# -*- coding: utf-8 -*-
import numpy as np

def getDetectorMatrix(fileName):
    file = open(fileName)
    matrix = np.loadtxt(file)
    file.close()
    return matrix

def broken_pixel_data_rstr(mass):

   for i in range(len(mass)):
       
       for j in range(len(mass[i])):
           if(mass[i][j] == 0):
               average = 0
               for sting in range(len(mass)):
                   average = average + mass[sting][j]

               if(average > (256*10)):

                   if((i < 1) or (i ==(len(mass) -1)) ): 
                       mass[i][j] = average/256
                       break
                   x1 = i -1
                   x2 = i+1
                   x = i
                   y1 = mass[x1][j]
                   y2 = mass[x2][j]
                   mass[i][j] = y1 + ((y2 - y1) * (x - x1))/(x2 - x1)