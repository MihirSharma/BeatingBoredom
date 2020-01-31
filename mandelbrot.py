import matplotlib.pyplot as plt
import numpy as np

x = 0.4
lsx = []
lsy = []
for i in range(4001):
    for j in range(50):
        x = i*0.001*x*(1-x)
        if(j > 50-17):
            lsx.append(float("{0:.3f}".format(i*0.001)))
            lsy.append(float("{0:.4f}".format(x)))
        
    print(x)
    x = 0.4
categories = np.random.randint(3,size = 4001*16)
colormap = np.array(['r','g','b'])
plt.scatter(lsx, lsy, c = colormap[categories]) 
# the reason for the color is to make the mandelbrot scattering visible at high values of i
plt.xlabel('Rate(r)')
plt.ylabel('p[n+1] = r * p[n] * (1-p[n])')
plt.show()
