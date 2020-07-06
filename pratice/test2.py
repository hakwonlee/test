
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import *

fig, ax=plt.subplots()
plt.subplots_adjust(left=0.25,bottom=0.25)

t=np.arange(0.0,1.0,0.001)

a0=5
f0=3

s=a0*np.sin(2*np.pi*f0*t)
l, = plt.plot(t,s,lw=2,color='red')
plt.axis([0,1,-10,10])

plt.show()