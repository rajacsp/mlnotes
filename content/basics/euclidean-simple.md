---
title: Euclidean-Simple
date: 2024-11-24
author: Your Name
cell_count: 4
score: 0
---

---
title: "Euclidean Simple"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import math
import numpy
from random import uniform
```


```python
def fastest_calc_dist(p1,p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 +
                     (p2[1] - p1[1]) ** 2 +
                     (p2[2] - p1[2]) ** 2)    

def math_calc_dist(p1,p2):
    return math.sqrt(math.pow((p2[0] - p1[0]), 2) +
                     math.pow((p2[1] - p1[1]), 2) +
                     math.pow((p2[2] - p1[2]), 2))

def numpy_calc_dist(p1,p2):
    return numpy.linalg.norm(numpy.array(p1)-numpy.array(p2))
```


```python
TOTAL_LOCATIONS = 1000

p1 = dict()
p2 = dict()
for i in range(0, TOTAL_LOCATIONS):
    p1[i] = (uniform(0,1000),uniform(0,1000),uniform(0,1000))
    p2[i] = (uniform(0,1000),uniform(0,1000),uniform(0,1000)) 

total_dist = 0
for i in range(0, TOTAL_LOCATIONS):
    for j in range(0, TOTAL_LOCATIONS):
        dist = fastest_calc_dist(p1[i], p2[j]) #change this line for testing
        total_dist += dist

print(total_dist)
```

    656157444.0241755



---
**Score: 0**