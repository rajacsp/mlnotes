---
title: Simple-Numba
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

---
title: "Numba Simple"
author: "Raja CSP Raman"
date: 2019-05-07
description: "-"
type: technical_note
draft: false
---

```python
from numba import njit, prange
import numpy as np

@njit(parallel=True)
def add(A):
    s = 0
    # Without "parallel=True" in the jit-decorator
    # the prange statement is equivalent to range
    for i in prange(A.shape[0]):
        s += A[i]
    return s
```


```python
abc = add(np.array([1, 2, 3]))
```


```python
abc
```




    6



More on Numba

http://numba.pydata.org/numba-doc/latest/user/parallel.html#numba-parallel

http://numba.pydata.org/numba-doc/latest/index.html


```python

```


---
**Score: 5**