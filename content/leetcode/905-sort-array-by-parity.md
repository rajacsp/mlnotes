---
title: 905-Sort-Array-By-Parity
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/sort-array-by-parity


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
  def sortArrayByParity(self, A: List[int]) -> List[int]:
    l = 0
    r = len(A) - 1

    while l < r:
      if A[l] % 2 == 1 and A[r] % 2 == 0:
        A[l], A[r] = A[r], A[l]
      if A[l] % 2 == 0:
        l += 1
      if A[r] % 2 == 1:
        r -= 1

    return A
```


```
new Solution().sortArrayByParity()
```


---
**Score: 5**