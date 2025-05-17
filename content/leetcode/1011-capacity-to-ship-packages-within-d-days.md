---
title: 1011-Capacity-To-Ship-Packages-Within-D-Days
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/capacity-to-ship-packages-within-d-days


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
  def shipWithinDays(self, weights: List[int], days: int) -> int:
    l = max(weights)
    r = sum(weights)

    def shipDays(shipCapacity: int) -> int:
      days = 1
      capacity = 0
      for weight in weights:
        if capacity + weight > shipCapacity:
          days += 1
          capacity = weight
        else:
          capacity += weight
      return days

    while l < r:
      m = (l + r) // 2
      if shipDays(m) <= days:
        r = m
      else:
        l = m + 1

    return l
```


```
new Solution().shipWithinDays()
```


---
**Score: 5**