---
title: 941-Valid-Mountain-Array
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/valid-mountain-array


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
  def validMountainArray(self, A: List[int]) -> bool:
    if len(A) < 3:
      return False

    l = 0
    r = len(A) - 1

    while l + 1 < len(A) and A[l] < A[l + 1]:
      l += 1
    while r > 0 and A[r] < A[r - 1]:
      r -= 1

    return l > 0 and r < len(A) - 1 and l == r
```


```
new Solution().validMountainArray()
```


---
**Score: 5**