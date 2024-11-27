---
title: New-Axis
date: 2024-11-27
author: Your Name
cell_count: 3
score: 0
---

```python

```


```python
import numpy as np

x1 = np.arange(1,10).reshape(3,3)
print(x1.shape)

x1_new = x1[:,np.newaxis]
print(x1_new.shape)

```

    (3, 3)
    (3, 1, 3)



```python

```


---
**Score: 0**