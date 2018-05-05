import numpy as np
import matplotlib.pyplot as plt

def Fx_function(x, y): 
	return x

def Fy_function(x, y): 
	return y

# The grid size, the arrows will be located on each of the grid points.  
WIDTH = 12
HEIGHT = 8
X, Y = np.mgrid[0:WIDTH, 0:HEIGHT]

# Vector properties: r is color, T is angle
# T = np.arctan2(Y - n / 2., X - n/2.)
# R = 10 + np.sqrt((Y - n / 2.0) ** 2 + (X - n / 2.0) ** 2)
# U, V = R * np.cos(T), R * np.sin(T)
X_GRAPH, Y_GRAPH = X - (WIDTH - 1) / 2., Y - (HEIGHT - 1) / 2.
U, V = X_GRAPH, Y_GRAPH
R = np.sqrt(U**2+V**2)
U, V = U / R, V / R


plt.axes([0.025, 0.025, 0.95, 0.95])
# plt.quiver(X, Y, U, V, R, alpha=.5)
# plt.quiver(X, Y, U, V, edgecolor='k', facecolor='None', linewidth=.5)
plt.quiver(X, Y, U, V, R)

plt.xlim(-1, WIDTH)
plt.xticks(())
plt.ylim(-1, HEIGHT)
plt.yticks(())

plt.show()