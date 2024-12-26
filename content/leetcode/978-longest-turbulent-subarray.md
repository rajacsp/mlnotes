---
title: 978-Longest-Turbulent-Subarray
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/longest-turbulent-subarray


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
  def maxTurbulenceSize(self, A: List[int]) -> int:
    ans = 1
    increasing = 1
    decreasing = 1

    for i in range(1, len(A)):
      if A[i] > A[i - 1]:
        increasing = decreasing + 1
        decreasing = 1
      elif A[i] < A[i - 1]:
        decreasing = increasing + 1
        increasing = 1
      else:
        increasing = 1
        decreasing = 1
      ans = max(ans, max(increasing, decreasing))

    return ans
```


```
new Solution().maxTurbulenceSize()
```


---
**Score: 5**