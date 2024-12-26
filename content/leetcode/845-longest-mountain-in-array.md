---
title: 845-Longest-Mountain-In-Array
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/longest-mountain-in-array


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
  def longestMountain(self, A: List[int]) -> int:
    ans = 0
    i = 0

    while i + 1 < len(A):
      while i + 1 < len(A) and A[i] == A[i + 1]:
        i += 1

      increasing = 0
      decreasing = 0

      while i + 1 < len(A) and A[i] < A[i + 1]:
        increasing += 1
        i += 1

      while i + 1 < len(A) and A[i] > A[i + 1]:
        decreasing += 1
        i += 1

      if increasing > 0 and decreasing > 0:
        ans = max(ans, increasing + decreasing + 1)

    return ans
```


```
new Solution().longestMountain()
```


---
**Score: 5**