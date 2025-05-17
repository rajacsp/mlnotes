---
title: 365-Water-And-Jug-Problem
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/water-and-jug-problem


```
import pyutil as pyu
pyu.get_local_pyinfo()
```


```
print(pyu.ps2("python-dotenv"))
```


```
from typing import List
```


```
class Solution:
  def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
    return targetCapacity == 0 or \
        jug1Capacity + jug2Capacity >= targetCapacity and \
        targetCapacity % gcd(jug1Capacity, jug2Capacity) == 0
```


```
new Solution().canMeasureWater()
```


---
**Score: 5**