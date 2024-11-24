---
title: Monte Carlo Pi
date: 2024-11-24
author: Your Name
cell_count: 4
score: 0
---

---
title: "Monte Carlo Pi"
author: "Raja CSP Raman"
date: 2019-05-07
description: "-"
type: technical_note
draft: false
---

```python
from numba import jit
import numpy as np
import random
import numba
```


```python
@numba.jit
def monte_carlo_pi(nsamples):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x**2 + y**2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples
```


```python
print(monte_carlo_pi(20))
```

    3.6



---
**Score: 0**