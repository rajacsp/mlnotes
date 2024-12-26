---
title: 875-Koko-Eating-Bananas
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/koko-eating-bananas


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
  def minEatingSpeed(self, piles: List[int], h: int) -> int:
    l = 1
    r = max(piles)

    # Hours to eat all piles with speed m
    def eatHours(m: int) -> int:
      return sum((pile - 1) // m + 1 for pile in piles)

    while l < r:
      m = (l + r) // 2
      if eatHours(m) <= h:
        r = m
      else:
        l = m + 1

    return l
```


```
new Solution().minEatingSpeed()
```


---
**Score: 5**