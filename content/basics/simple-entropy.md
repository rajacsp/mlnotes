---
title: Simple-Entropy
date: 2024-12-25
author: Your Name
cell_count: 6
score: 5
---

---
title: "Simple Entropy"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import math
from collections import Counter
import timeit
import numpy as np
```


```python
def eta(data, unit='natural'):
    base = {
        'shannon' : 2.,
        'natural' : math.exp(1),
        'hartley' : 10.
    }

    if len(data) <= 1:
        return 0

    counts = Counter()

    for d in data:
        counts[d] += 1

    ent = 0

    probs = [float(c) / len(data) for c in counts.values()]
    for p in probs:
        if p > 0.:
            ent -= p * math.log(p, base[unit])

    return ent
```


```python
eta(['Canada', 'is', 'the', 'sweetest', 'country'])
```




    1.6094379124341005




```python
repeat_number = 1000
e = timeit.repeat(
    stmt='''eta(labels)''', 
    setup='''labels=[1,3,5,2,3,5,3,2,1,3,4,5];from __main__ import eta''', 
    repeat=3, 
    number=repeat_number)
```


```python
print('Method: {}, Avg.: {:.6f}'.format("eta", np.array(e).mean()))
```

    Method: eta, Avg.: 0.010078



---
**Score: 5**