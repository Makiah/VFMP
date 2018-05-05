# Vector Field Motion Profiling

*Please note that this is incomplete, but explains the general idea behind using vector fields to profile a curve.* 

From what I can gather through experimental results, path generation via vector fields are simple: 
```
y = ax^3 + bx^2 + cx + d
F_x(x, y) = (-dy/dx + 1)(-y + ax^3 + bx^2 + cx + d) + x solved for y
F_y(x, y) = (-dx/dy + 1)(-y + ax^3 + bx^2 + cx + d) + y solved for x
```

These fields can be used to profile a robot to a given spline, provided you know the equation for the spline and the robot's approximate <x,y> position vector.  

## Example of field generation
![Example GIF](example/example.gif)

## Desmos-Based Example

Now uses derivative as a coefficient for more advanced correction

### XY Correction 
![Combined Correction](example/sine/xycorrection.png)

### Path Correction 
![Combined Correction](example/sine/pathcorrection.png)

### XY Correction 
![Combined Correction](example/sine/combinedcorrection.png)

## Legacy Work

### X Correction
![X Correction](example/parabola/xcorrection.png)

### Y Correction
![Y Correction](example/parabola/ycorrection.png)

### XY Correction
![XY Correction](example/parabola/xycorrection.png)

### Path Correction (x^2)
![Path Correction](example/parabola/pathcorrection.png)

### Combined Correction
![Combined Correction](example/parabola/combinedcorrection.png)
