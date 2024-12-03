---
title: Donut-Plot
date: 2024-12-03
author: Your Name
cell_count: 6
score: 5
---

---
title: "Donut Plot"
author: "Rj"
date: 2020-08-20
description: "Donut Plot"
type: technical_note
draft: false
---
Source:

https://matplotlib.org/3.1.1/gallery/pie_and_polar_charts/nested_pie.html


```python
import matplotlib.pyplot as plt
import numpy as np
```


```python
fig, ax = plt.subplots()

size = 0.3
vals = np.array([[60, 32], [37, 40]])

cmap = plt.get_cmap("tab20c")
# https://matplotlib.org/3.3.1/tutorials/colors/colormaps.html

# print(cmap)

outer_colors = cmap(np.arange(3)*4)
inner_colors = cmap(np.array([1, 2, 5, 6, 9, 10]))

ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors, wedgeprops=dict(width=size, edgecolor='w'))

ax.pie(vals.flatten(), radius=1-size, colors=inner_colors, wedgeprops=dict(width=size, edgecolor='w'))

# ax.set(aspect="equal", title='Pie plot with `ax.pie`')
plt.show()
```


    
![png](/mlnotes/images/donut-plot_3_0.png)
    



```python

```


```python

```


---
**Score: 5**