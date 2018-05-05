import numpy as np
import matplotlib.pyplot as plt

def Fx_function(x, y): 
	return x

def Fy_function(x, y): 
	return y

# The grid size, the arrows will be located on each of the grid points.  
n = 8
X, Y = np.mgrid[0:n, 0:n]

# Vector properties: r is color, T is angle
# T = np.arctan2(Y - n / 2., X - n/2.)
# R = 10 + np.sqrt((Y - n / 2.0) ** 2 + (X - n / 2.0) ** 2)
# U, V = R * np.cos(T), R * np.sin(T)
U, V = X, Y
R = np.sqrt(U**2+V**2)
U, V = U / R, V / R


plt.axes([0.025, 0.025, 0.95, 0.95])
# plt.quiver(X, Y, U, V, R, alpha=.5)
# plt.quiver(X, Y, U, V, edgecolor='k', facecolor='None', linewidth=.5)
plt.quiver(X, Y, U, V, R)

plt.xlim(-1, n)
plt.xticks(())
plt.ylim(-1, n)
plt.yticks(())

plt.show()