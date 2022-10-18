import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 1000)
y = np.sin(x)
z = np.cos(x)
fig, ax = plt.subplots()
fig.set_size_inches(10, 10)
ax.plot(x,y,x,z)
plt.show() # lance la fenetre backend (en fonction des settings)
fig.savefig('trigo.png')