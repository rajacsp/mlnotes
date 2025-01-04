---
title: 780-Reaching-Points
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/reaching-points


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
  def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
    while sx < tx and sy < ty:
      tx, ty = tx % ty, ty % tx

    return sx == tx and sy <= ty and (ty - sy) % tx == 0 or \
        sy == ty and sx <= tx and (tx - sx) % ty == 0
```


```
new Solution().reachingPoints()
```


---
**Score: 5**