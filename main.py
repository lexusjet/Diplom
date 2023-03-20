import getDetectorMatrix
import lexus_utility as lexus
import MonochoramtorLogClass as mlc
import Methods as methods

import matplotlib.pyplot as plt  
import numpy as np
from functools import reduce
from mpl_toolkits.mplot3d import Axes3D
import os.path

   

n = 0
k = 0

t = 1
test1 = [0,105,107,107,117]
test2 = [256,135,129,118,129]
# horisontal borders
hb1 = test1[t]
hb2 = test2[t]
# vertical borders
htest1 = [0,10,50,100,120]
htest2 = [256,246,206,156,136]
t = 0
vb1 = htest1[t]
vb2 = htest2[t]

fig, axs = plt.subplots(nrows= 3 , ncols= 1 )
fig. suptitle('Сравнение двух методов (слева новый, справа старый)\n  в границах  [{}:{},  {}:{}]'.format(vb1,vb2,hb1, hb2))

index = 0




path ="spectrs_{}"
spectreFileName = "{}_Event.txt"
spectreFileName = "{}_iToT.txt"
logFileName = "Log_{}.txt"


arr = []

while(os.path.exists(path.format(n))):
    method_firs_anser = []
    integral_method_anser = []
    pathFileName = os.path.join(path.format(n), spectreFileName)
    
    while(os.path.exists(pathFileName.format(k))):      
        mass =  np.array(getDetectorMatrix.getDetectorMatrix(pathFileName.format(k)))
        mass = mass[vb1:vb2, hb1:hb2]
        if(not len(arr) and n ==2 and k == 20): arr = mass[128]
        integral_method_anser.append(methods.IntegralMethod(mass))
        method_firs_anser.append(abs(min(methods.method(mass))))
        
        k = k + 1

        
    log = mlc.MonochoramtorLog(os.path.join(path.format(n), logFileName.format(n)))
    xValues = list(map(lambda x: x/4700 ,range(log.engineStart, log.engineStop+log.engineStep, log.engineStep)))      
    

    # axs[n].plot(xValues, integral_method_anser)   
    axs[n].plot(xValues, method_firs_anser)
    axs.ravel()[index].set_title(pathFileName.split("\\")[0].format(n))
    index +=1
    # axs.ravel()[index].set_title(pathFileName.split("\\")[0].format(n))
    # index +=1

         
    n += 1    
    k = 0
    
fig.tight_layout()






