---
title: 598-Range-Addition-Ii
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/range-addition-ii


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
  def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
    minY = m
    minX = n

    for y, x in ops:
      minY = min(minY, y)
      minX = min(minX, x)

    return minX * minY
```


```
new Solution().maxCount()
```


---
**Score: 5**