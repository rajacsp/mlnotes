---
title: Star-Plot
date: 2024-12-14
author: Your Name
cell_count: 3
score: 0
---

```python

```


```python
import numpy as np
import matplotlib.pyplot as plt


x = np.random.rand(10)
y = np.random.rand(10)
z = np.sqrt(x**2 + y**2)

plt.subplot(111)
plt.scatter(x, y, s=500, c=z, marker=">")

plt.show()
```


```python

```


---
**Score: 0**