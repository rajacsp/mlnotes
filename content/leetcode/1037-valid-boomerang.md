---
title: 1037-Valid-Boomerang
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/valid-boomerang


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
  def isBoomerang(self, points: List[List[int]]) -> bool:
    return (points[1][0] - points[0][0]) * (points[2][1] - points[1][1]) != \
        (points[1][1] - points[0][1]) * (points[2][0] - points[1][0])
```


```
new Solution().isBoomerang()
```


---
**Score: 5**