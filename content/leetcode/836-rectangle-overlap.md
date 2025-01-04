---
title: 836-Rectangle-Overlap
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/rectangle-overlap


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
  def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
    return rec1[0] < rec2[2] and rec2[0] < rec1[2] and rec1[1] < rec2[3] and rec2[1] < rec1[3]
```


```
new Solution().isRectangleOverlap()
```


---
**Score: 5**