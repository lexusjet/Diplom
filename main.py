import getDetectorMatrix
import lexus_utility as lexus
import MonochoramtorLogClass as mlc
import Methods as methods

import matplotlib.pyplot as plt  
import numpy as np
from functools import reduce
from mpl_toolkits.mplot3d import Axes3D
import os.path


# horisontal borders
hb1, hb2 = 100,150
# vertical borders
vb1, vb2  = 0,256


path ="spectrs_{}"
spectreFileName = "{}_Event.txt"

ansers = {0: [], 1: []}
n = 0
while(os.path.exists(path.format(n))):
    k = 0
    method_firs_anser = []
    integral_method_anser = []
    pathFileName = os.path.join(path.format(n), spectreFileName)
    
    while(os.path.exists(pathFileName.format(k))):      
        mass =  np.array(getDetectorMatrix.getDetectorMatrix(pathFileName.format(k)))
        mass = getDetectorMatrix.spectrumPreparation(mass)
        mass = mass[vb1:vb2, hb1:hb2]
        mass = np.sum(mass,0).dot(1/len(mass))
        integral_method_anser.append(methods.IntegralMethod(mass))
        method_firs_anser.append(abs(min(methods.method(mass))))
        
        k = k + 1
        
    ansers[0].append(integral_method_anser)
    ansers[1].append(method_firs_anser)
     
    n += 1    
 
  
  
logFileName = "Log_{}.json"
fig, axs = plt.subplots(nrows= len(ansers[0]) , ncols= len(ansers))
fig. suptitle('Новый и старый \n  в границах  [{}:{},  {}:{}]'.format(vb1,vb2,hb1, hb2))   
index = 0
for i in range(len(ansers[0])):
    for j in range(len(ansers)):
        log = mlc.MonochoramtorLog()
        log.loadFromJson(os.path.join(path.format(i), logFileName.format(i)))
        xValues = list(map(lambda x: x/4700 ,range(log.engineStart, log.engineStop+log.engineStep, log.engineStep)))
        axs[i,j].plot(xValues, ansers[j][i])
        axs.ravel()[index].set_title(path.format(i))
        index += 1

fig.tight_layout()






