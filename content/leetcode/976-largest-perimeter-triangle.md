---
title: 976-Largest-Perimeter-Triangle
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/largest-perimeter-triangle


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
  def largestPerimeter(self, A: List[int]) -> int:
    A = sorted(A)

    for i in range(len(A) - 1, 1, -1):
      if A[i - 2] + A[i - 1] > A[i]:
        return A[i - 2] + A[i - 1] + A[i]

    return 0
```


```
new Solution().largestPerimeter()
```


---
**Score: 5**