---
title: 896-Monotonic-Array
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/monotonic-array


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
  def isMonotonic(self, A: List[int]) -> bool:
    increasing = True
    decreasing = True

    for i in range(1, len(A)):
      increasing &= A[i - 1] <= A[i]
      decreasing &= A[i - 1] >= A[i]

    return increasing or decreasing
```


```
new Solution().isMonotonic()
```


---
**Score: 5**