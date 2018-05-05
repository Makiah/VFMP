import numpy as np
import matplotlib.pyplot as plt
from sympy import *

# The axes displayed on the graph.  
plt.axes([0.025, 0.025, 0.95, 0.95])
WIDTH = 40
HEIGHT = 30

# Use the amazingness of sympy to figure out the spline to use.  
spline_string = input("f(x) = y = ")
spline_parsed = sympify(spline_string)
lookahead_factor = float(input("lookahead (0-1): "))

# Interpret the spline using "sympify"
x = Symbol("x")
print("Parsed function is " + str(spline_parsed))

# Graph the actual function by sampling points along x values.  
x_vals = np.arange(0, WIDTH, .1)
lam_x = lambdify(x, spline_parsed, modules=['numpy'])
y_vals = lam_x(x_vals - (WIDTH - 1) / 2) + (HEIGHT - 1) / 2
plt.plot(x_vals, y_vals)

# Graph the vector field (which matplotlib calls a "quiver")
print("")
y = Symbol("y")
actual_equation = sympify(str(spline_parsed) + " - y")
print("Actually using equation f(x,y) = " + str(actual_equation))
dfdx = diff(actual_equation, x) # partial derivative with respect to x
dfdy = diff(actual_equation, y) # partial derivative with respect to y
print("df/dx = " + str(dfdx)) 
print("df/dy = " + str(dfdy))

# Solve for x in terms of y
xfory = solve(actual_equation, y)[0]
print("x solved for y: " + str(xfory))

# Solve for y in terms of x
yforx = solve(actual_equation, x)[0] # returns multiple
print("y solved for x: " + str(yforx))

# The grid size, the arrows will be located on each of the grid points.  
X, Y = np.mgrid[0:WIDTH, 0:HEIGHT]

# Where the vector would be positioned on the x and y grid (the np.grid makes this weird)
X_GRAPH, Y_GRAPH = X - (WIDTH - 1) / 2., Y - (HEIGHT - 1) / 2.

# Use calculus I figured out experimentally to determine the vector x and y components.  SymPy makes this extremely easy.  
dfdx_lam = lambdify([x, y], dfdx, modules=['numpy'])
dfdy_lam = lambdify([x, y], dfdy, modules=['numpy'])
actual_lam = lambdify([x, y], actual_equation, modules=['numpy'])
yforx_lam = lambdify([x, y], yforx, modules=['numpy'])
xfory_lam = lambdify([x, y], xfory, modules=['numpy'])
U = lookahead_factor * (-1 * dfdx_lam(X_GRAPH, Y_GRAPH) * actual_lam(X_GRAPH, Y_GRAPH)) + (yforx_lam(X_GRAPH, np.abs(Y_GRAPH)))
V = lookahead_factor * (-1 * dfdy_lam(X_GRAPH, Y_GRAPH) * actual_lam(X_GRAPH, Y_GRAPH)) + (xfory_lam(X_GRAPH, Y_GRAPH))

# Normalize the vector magnitudes to improve their appearance, otherwise we get weird, miniscule vectors.  
R = np.sqrt(U**2+V**2)  # color of the vector
U, V = U / R, V / R     # normalized x and y

# Actually graph the vector field.  
plt.quiver(X, Y, U, V, R, pivot="middle")

# Define the width and height of the graph
plt.xlim(0, WIDTH)
plt.xticks(())
plt.ylim(0, HEIGHT)
plt.yticks(())

# Show the graph
plt.show()