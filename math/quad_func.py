import matplotlib.pylab as plt
import numpy as np

x,y=[],[]

def quad_func(x):
    y = x**2 + 2*x + 1
    return y

for _x in np.linspace(-11,9,40):
    x.append(_x)
    y.append(quad_func(_x))

plt.plot(x,y)
plt.show()

