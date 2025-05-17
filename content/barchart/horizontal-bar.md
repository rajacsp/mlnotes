---
title: Horizontal-Bar
date: 2025-05-17
author: Your Name
cell_count: 3
score: 0
---

```python
# http://matplotlib.org/1.2.1/examples/pylab_examples/barh_demo.html
```


```python
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
 

val = [4, 6, 21]
pos = np.arange(len(val)) + .5    # the bar centers on the y axis

pl.figure(1)
plt.barh(pos, val, align='center')
plt.yticks(pos, ('A', 'B', 'C'))
plt.xlabel('Performance')
plt.title('How fast do you want to go today?')
plt.grid(True)

plt.show()
```


    
![png](/mlnotes/images/horizontal-bar_1_0.png)
    



```python

```


---
**Score: 0**