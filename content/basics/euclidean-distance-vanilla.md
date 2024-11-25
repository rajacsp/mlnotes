---
title: Euclidean-Distance-Vanilla
date: 2024-11-25
author: Your Name
cell_count: 6
score: 5
---

---
title: "Euclidean Distance Vanilla"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import numpy
```


```python
def dist(x,y):   
    return numpy.sqrt(numpy.sum((x-y)**2))
```


```python
a = numpy.array((1,2,3))
b = numpy.array((4,5,6))
dist_a_b = dist(a,b)
```


```python
print(dist_a_b)
```

    5.196152422706632



```python

```


---
**Score: 5**