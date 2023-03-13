import getDetectorMatrix
import lexus_utility as lexus

import matplotlib.pyplot as plt  
import numpy as np
from functools import reduce
from mpl_toolkits.mplot3d import Axes3D
import os.path

   

n = 0
k = 0



# g = plt.GridSpec(18,2)
# fig = plt.figure()

path = os.path.join("spectrs_{}", "{}_Event.txt")


while(os.path.exists(path.format(n, k))):
    arr = []
    while(os.path.exists(path.format(n, k))):
        mass =  np.array(getDetectorMatrix.getDetectorMatrix(path.format(n,k)))
        arr.append(reduce(lambda a, b : a + b , mass[:256, 100:143]))
        k = k + 1
        
        
    
    # s = fig.add_subplot(g[(n*5):(n*5+5),0])
    # s.plot(range(len(arr)), list(map(sum,arr)))
    # s.set_title(path.split("\\")[0].format(n))
    # s = fig.add_subplot(g[(n*5):(n*5+5),1], projection='3d') 
   
    fig = plt.figure()
    s = Axes3D(fig)
   
    X = range(len(arr[0]))
    Y = range(len(arr))    
    X,Y = np.meshgrid(X,Y)
    s.plot_surface(X, Y, np.array(arr), rstride=1, cstride=1, cmap=plt.cm.hot)
    s.set_title(path.split("\\")[0].format(n))
    
    n += 1
    k = 0



plt.show()





