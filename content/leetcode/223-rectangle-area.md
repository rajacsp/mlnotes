---
title: 223-Rectangle-Area
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/rectangle-area


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
  def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
    x = min(C, G) - max(A, E) if max(A, E) < min(C, G) else 0
    y = min(D, H) - max(B, F) if max(B, F) < min(D, H) else 0
    return (C - A) * (D - B) + (G - E) * (H - F) - x * y
```


```
new Solution().computeArea()
```


---
**Score: 5**