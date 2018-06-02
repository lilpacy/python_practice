import matplotlib.pylab as plt
import math

x,y=[],[]

for _x in range(-360,360,5):
    x.append(math.radians(_x))
    y.append(math.cos(math.radians(_x)))

plt.plot(x,y)
plt.axis(ymin=-1.5,ymax=1.5)
plt.show()
