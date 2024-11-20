---
title: Add-Even-Indices
date: 2024-11-20
author: Your Name
cell_count: 5
score: 5
---

```python
from numba import njit, prange
import numpy as np
```


```python
@njit(parallel=True)
def add_even_indices(A):
    s = 0
    # Without "parallel=True" in the jit-decorator
    # the prange statement is equivalent to range
    for i in prange(A.shape[0]):
        if(i % 2 == 0):
            s += A[i]
    return s
```


```python
abc = add_even_indices(np.array([1, 2, 3, 4, 5, 6]))
```


```python
abc
```




    9




```python

```


---
**Score: 5**