---
title: 883-Projection-Area-Of-3D-Shapes
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/projection-area-of-3d-shapes


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
  def projectionArea(self, grid: List[List[int]]) -> int:
    return sum(a > 0 for row in grid for a in row) + sum(max(row) for row in grid) + sum(max(col) for col in zip(*grid))
```


```
new Solution().projectionArea()
```


---
**Score: 5**