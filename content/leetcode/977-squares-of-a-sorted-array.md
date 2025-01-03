---
title: 977-Squares-Of-A-Sorted-Array
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/squares-of-a-sorted-array


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
  def sortedSquares(self, A: List[int]) -> List[int]:
    n = len(A)
    l = 0
    r = n - 1
    ans = [0] * n

    while n:
      n -= 1
      if abs(A[l]) > abs(A[r]):
        ans[n] = A[l] * A[l]
        l += 1
      else:
        ans[n] = A[r] * A[r]
        r -= 1

    return ans
```


```
new Solution().sortedSquares()
```


---
**Score: 5**