---
title: Timeit-Simple
date: 2024-12-07
author: Your Name
cell_count: 5
score: 5
---

---
title: "Timeit Simple"
author: "Rj"
date: 2019-04-24
description: "-"
type: technical_note
draft: false
---

```python
import timeit
import numpy as np
```


```python
def add(x, y):
    return x + y
```


```python
repeat_number = 100000
e = timeit.repeat(
    stmt='''add(a, b)''', 
    setup='''a=2; b=3;from __main__ import add''', 
    repeat=3,
    number=repeat_number)
```


```python
print('Method: {}, Avg.: {:.6f}'.format("eta", np.array(e).mean()))
```

    Method: eta, Avg.: 0.009691



---
**Score: 5**