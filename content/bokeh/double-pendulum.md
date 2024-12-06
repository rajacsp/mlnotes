---
title: Double-Pendulum
date: 2024-12-06
author: Your Name
cell_count: 5
score: 5
---

```python

```


```python
from bokeh.plotting import figure, output_file, show
from bokeh.io import output_notebook
from bokeh.models import ColumnDataSource
```


```python
# Set Bokeh output to notebook
output_notebook()
```


<style>
    .bk-notebook-logo {
        display: block;
        width: 20px;
        height: 20px;
        background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAABx0RVh0U29mdHdhcmUAQWRvYmUgRmlyZXdvcmtzIENTNui8sowAAAOkSURBVDiNjZRtaJVlGMd/1/08zzln5zjP1LWcU9N0NkN8m2CYjpgQYQXqSs0I84OLIC0hkEKoPtiH3gmKoiJDU7QpLgoLjLIQCpEsNJ1vqUOdO7ppbuec5+V+rj4ctwzd8IIbbi6u+8f1539dt3A78eXC7QizUF7gyV1fD1Yqg4JWz84yffhm0qkFqBogB9rM8tZdtwVsPUhWhGcFJngGeWrPzHm5oaMmkfEg1usvLFyc8jLRqDOMru7AyC8saQr7GG7f5fvDeH7Ej8CM66nIF+8yngt6HWaKh7k49Soy9nXurCi1o3qUbS3zWfrYeQDTB/Qj6kX6Ybhw4B+bOYoLKCC9H3Nu/leUTZ1JdRWkkn2ldcCamzrcf47KKXdAJllSlxAOkRgyHsGC/zRday5Qld9DyoM4/q/rUoy/CXh3jzOu3bHUVZeU+DEn8FInkPBFlu3+nW3Nw0mk6vCDiWg8CeJaxEwuHS3+z5RgY+YBR6V1Z1nxSOfoaPa4LASWxxdNp+VWTk7+4vzaou8v8PN+xo+KY2xsw6une2frhw05CTYOmQvsEhjhWjn0bmXPjpE1+kplmmkP3suftwTubK9Vq22qKmrBhpY4jvd5afdRA3wGjFAgcnTK2s4hY0/GPNIb0nErGMCRxWOOX64Z8RAC4oCXdklmEvcL8o0BfkNK4lUg9HTl+oPlQxdNo3Mg4Nv175e/1LDGzZen30MEjRUtmXSfiTVu1kK8W4txyV6BMKlbgk3lMwYCiusNy9fVfvvwMxv8Ynl6vxoByANLTWplvuj/nF9m2+PDtt1eiHPBr1oIfhCChQMBw6Aw0UulqTKZdfVvfG7VcfIqLG9bcldL/+pdWTLxLUy8Qq38heUIjh4XlzZxzQm19lLFlr8vdQ97rjZVOLf8nclzckbcD4wxXMidpX30sFd37Fv/GtwwhzhxGVAprjbg0gCAEeIgwCZyTV2Z1REEW8O4py0wsjeloKoMr6iCY6dP92H6Vw/oTyICIthibxjm/DfN9lVz8IqtqKYLUXfoKVMVQVVJOElGjrnnUt9T9wbgp8AyYKaGlqingHZU/uG2NTZSVqwHQTWkx9hxjkpWDaCg6Ckj5qebgBVbT3V3NNXMSiWSDdGV3hrtzla7J+duwPOToIg42ChPQOQjspnSlp1V+Gjdged7+8UN5CRAV7a5EdFNwCjEaBR27b3W890TE7g24NAP/mMDXRWrGoFPQI9ls/MWO2dWFAar/xcOIImbbpA3zgAAAABJRU5ErkJggg==);
    }
</style>
<div>
    <a href="https://bokeh.org" target="_blank" class="bk-notebook-logo"></a>
    <span id="d547ee87-e3c4-4c8b-92cf-7487071dc34c">Loading BokehJS ...</span>
</div>






```python
import numpy as np
from scipy.integrate import solve_ivp
from bokeh.plotting import figure, show

# Double pendulum parameters
g = 9.8  # gravity (m/s^2)
L1 = 1.0  # length of the first pendulum (m)
L2 = 1.0  # length of the second pendulum (m)
m1 = 1.0  # mass of the first pendulum (kg)
m2 = 1.0  # mass of the second pendulum (kg)

# Double pendulum equations
def double_pendulum(t, y):
    theta1, z1, theta2, z2 = y
    delta = theta2 - theta1

    denominator1 = (m1 + m2) * L1 - m2 * L1 * np.cos(delta)**2
    denominator2 = (L2 / L1) * denominator1

    theta1_dot = z1
    theta2_dot = z2

    z1_dot = (
        m2 * L1 * z1**2 * np.sin(delta) * np.cos(delta)
        + m2 * g * np.sin(theta2) * np.cos(delta)
        + m2 * L2 * z2**2 * np.sin(delta)
        - (m1 + m2) * g * np.sin(theta1)
    ) / denominator1

    z2_dot = (
        -m2 * L2 * z2**2 * np.sin(delta) * np.cos(delta)
        + (m1 + m2) * g * np.sin(theta1) * np.cos(delta)
        - (m1 + m2) * L1 * z1**2 * np.sin(delta)
        - (m1 + m2) * g * np.sin(theta2)
    ) / denominator2

    return [theta1_dot, z1_dot, theta2_dot, z2_dot]

# Initial conditions and time steps
theta1_0 = np.pi / 2  # initial angle of pendulum 1
theta2_0 = np.pi / 4  # initial angle of pendulum 2
z1_0 = 0.0  # initial angular velocity of pendulum 1
z2_0 = 0.0  # initial angular velocity of pendulum 2
y0 = [theta1_0, z1_0, theta2_0, z2_0]

t = np.linspace(0, 20, 10000)  # time array

# Solve the system
solution = solve_ivp(double_pendulum, [t[0], t[-1]], y0, t_eval=t, method="RK45")
theta1 = solution.y[0]
theta2 = solution.y[2]

# Convert to Cartesian coordinates
x1 = L1 * np.sin(theta1)
y1 = -L1 * np.cos(theta1)
x2 = x1 + L2 * np.sin(theta2)
y2 = y1 - L2 * np.cos(theta2)

# Use the trajectories of the second pendulum for plotting
num_segments = 7
xs = np.array_split(x2, num_segments)
ys = np.array_split(y2, num_segments)

# Define a color palette
colors = ["#F7FCF0", "#E0F3DB", "#CCEBC5", "#A8DDB5", "#7BCCC4", "#43A2CA", "#0868AC"]

# Create the Bokeh figure
p = figure(title="Double Pendulum Visualization",
           background_fill_color="#f9f9f9",
           x_axis_label="X",
           y_axis_label="Y",
           match_aspect=True)

# Add the multi_line glyph
p.multi_line(xs, ys, line_color=colors, line_alpha=0.8, line_width=1.5)

# Show the plot
show(p)
```



<div id="c1f3a5ee-5b13-41df-9646-d1b5fc4ea1d9" data-root-id="p1001" style="display: contents;"></div>






```python

```


---
**Score: 5**