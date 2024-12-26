---
title: Chua-Circuit
date: 2024-12-26
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
    <span id="ed87caa2-9d77-4126-9db2-e8b01a9467c4">Loading BokehJS ...</span>
</div>






```python
import numpy as np
from scipy.integrate import odeint
from bokeh.plotting import figure, show

# Chua's Circuit parameters
alpha = 15.6
beta = 28.0

# Piecewise linear function for the Chua circuit
def chua_m(x):
    m0 = -1.143
    m1 = -0.714
    return m1 * x + 0.5 * (m0 - m1) * (np.abs(x + 1) - np.abs(x - 1))

# Chua's Circuit function
def chua_circuit(state, t):
    x, y, z = state
    x_dot = alpha * (y - x - chua_m(x))
    y_dot = x - y + z
    z_dot = -beta * y
    return [x_dot, y_dot, z_dot]

# Initial conditions and time steps
initial = [0.7, 0, 0]
t = np.linspace(0, 100, 10000)

# Solve Chua's Circuit equations
solution = odeint(chua_circuit, initial, t)
x = solution[:, 0]
y = solution[:, 1]
z = solution[:, 2]

# Rotate the data for a different perspective
theta = np.pi / 4
xprime = np.cos(theta) * x - np.sin(theta) * y

# Split data into segments for multi-line
num_segments = 7
xs = np.array_split(xprime, num_segments)
ys = np.array_split(z, num_segments)

# Define a color palette
colors = ["#F0F9E8", "#BAE4BC", "#7BCCC4", "#43A2CA", "#0868AC", "#084081", "#041D54"]

# Create the Bokeh figure
p = figure(title="Chua's Circuit Visualization",
           background_fill_color="#f9f9f9",
           x_axis_label="X'",
           y_axis_label="Z")

# Add the multi_line glyph
p.multi_line(xs, ys, line_color=colors, line_alpha=0.8, line_width=1.5)

# Show the plot
show(p)
```



<div id="b277f002-a2fa-4e0d-ae71-f7efdfa8235f" data-root-id="p1001" style="display: contents;"></div>






```python

```


---
**Score: 5**