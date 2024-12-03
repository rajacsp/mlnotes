---
title: Euclidean-Distance
date: 2024-12-03
author: Your Name
cell_count: 4
score: 0
---

---
title: "Euclidean Distance"
author: "Raja CSP Raman"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
def euclidean_distance(p, q):

    #make sure both array are in the same dimension
    assert len(p) == len(q)  

    return max([abs(x-y) for x,y in zip(p,q)])
```


```python
acb = euclidean_distance([1,2,3],[1, 2, 3])
print(acb)
```

    0



```python

```


---
**Score: 0**