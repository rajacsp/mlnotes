---
title: 786-K-Th-Smallest-Prime-Fraction
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/k-th-smallest-prime-fraction


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
  def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
    n = len(A)
    ans = [0, 1]
    l = 0
    r = 1

    while True:
      m = (l + r) / 2
      ans[0] = 0
      count = 0
      j = 1

      for i in range(n):
        while j < n and A[i] > m * A[j]:
          j += 1
        count += n - j
        if j == n:
          break
        if ans[0] * A[j] < ans[1] * A[i]:
          ans[0] = A[i]
          ans[1] = A[j]

      if count < K:
        l = m
      elif count > K:
        r = m
      else:
        return ans
```


```
new Solution().kthSmallestPrimeFraction()
```


---
**Score: 5**