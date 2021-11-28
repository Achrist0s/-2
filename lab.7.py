import matplotlib.pyplot as plt
import numpy as np 

fig, ax = plt.subplot()

x = np.linspace(0, 10, 100)
y = x**np.cos(x**2)

ax.plot (x, y)

plt.show()