---
title: 922-Sort-Array-By-Parity-Ii
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/sort-array-by-parity-ii


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
  def sortArrayByParityII(self, A: List[int]) -> List[int]:
    n = len(A)

    i = 0
    j = 1
    while i < n:
      while i < n and A[i] % 2 == 0:
        i += 2
      while j < n and A[j] % 2 == 1:
        j += 2
      if i < n:
        A[i], A[j] = A[j], A[i]
      i += 2
      j += 2

    return A
```


```
new Solution().sortArrayByParityII()
```


---
**Score: 5**