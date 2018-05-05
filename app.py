import numpy as np
import matplotlib.pyplot as plt
from sympy import *

# The axes displayed on the graph.  
plt.axes([0.025, 0.025, 0.95, 0.95])
WIDTH = 40
HEIGHT = 8

# Use the amazingness of sympy to figure out the spline to use.  
spline_string = input("f(x,y) = y = ")
spline_parsed = sympify(spline_string)

# Interpret the spline
x = Symbol("x")
# y = Symbol("y")
print("Parsed function is " + str(spline_parsed))
# print("x = 0 and y = 0 is " + str(spline_parsed.subs({x: 0, y: 0})))

# GRAPHING ACTUAL FUNCTION
x_vals = np.arange(0, WIDTH, .1)
lam_x = lambdify(x, spline_parsed, modules=['numpy'])
y_vals = lam_x(x_vals - (WIDTH - 1) / 2) + (HEIGHT - 1) / 2
plt.plot(x_vals, y_vals)

# GRAPHING VECTOR FIELD 
dfdx = diff(spline_parsed, x)
# dfdy = diff(spline_parsed, y)
print("df/dx = " + str(dfdx)) # AWESOME
# print("df/dy = " + str(dfdy))

# The grid size, the arrows will be located on each of the grid points.  
X, Y = np.mgrid[0:WIDTH, 0:HEIGHT]

# Vector properties: r is color, T is angle
# T = np.arctan2(Y - n / 2., X - n/2.)
# R = 10 + np.sqrt((Y - n / 2.0) ** 2 + (X - n / 2.0) ** 2)
# U, V = R * np.cos(T), R * np.sin(T)
X_GRAPH, Y_GRAPH = X - (WIDTH - 1) / 2., Y - (HEIGHT - 1) / 2.

# Define the two graph equations here, using X_GRAPH and Y_GRAPH as input parameters.  
U, V = X_GRAPH*2, Y_GRAPH

# Normalize the vector magnitudes to improve their appearance, otherwise we get weird, miniscule vectors.  
R = np.sqrt(U**2+V**2)  # color of the vector
U, V = U / R, V / R     # normalized x and y

# Actually graph the vector field.  
plt.quiver(X, Y, U, V, R)
# plt.quiver(X, Y, U, V, R, alpha=.5)
# plt.quiver(X, Y, U, V, edgecolor='k', facecolor='None', linewidth=.5)

plt.xlim(0, WIDTH)
plt.xticks(())
plt.ylim(0, HEIGHT)
plt.yticks(())

plt.show()