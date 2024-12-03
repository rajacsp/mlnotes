---
title: Numba Benchmark
date: 2024-12-03
author: Your Name
cell_count: 6
score: 5
---

---
title: "Numba Benchmark"
author: "Raja CSP Raman"
date: 2019-05-07
description: "-"
type: technical_note
draft: false
---

```python
from numba import jit
import numpy as np
import time
```


```python
x = np.arange(100).reshape(10, 10)

@jit(nopython=True)
def go_fast(a): # Function is compiled and runs in machine code
    trace = 0
    for i in range(a.shape[0]):
        trace += np.tanh(a[i, i])
    return a + trace
```


```python
start = time.time()
go_fast(x)
end = time.time()
print("Elapsed (with compilation) = %s" % (end - start))
```

    Elapsed (with compilation) = 0.14084887504577637



```python
start = time.time()
go_fast(x)
end = time.time()
print("Elapsed (after compilation) = %s" % (end - start))
```

    Elapsed (after compilation) = 5.1975250244140625e-05



```python

```


---
**Score: 5**