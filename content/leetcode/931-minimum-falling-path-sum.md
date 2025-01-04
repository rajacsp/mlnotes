---
title: 931-Minimum-Falling-Path-Sum
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/minimum-falling-path-sum


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
  def minFallingPathSum(self, A: List[List[int]]) -> int:
    n = len(A)

    for i in range(1, n):
      for j in range(n):
        mini = math.inf
        for k in range(max(0, j - 1), min(n, j + 2)):
          mini = min(mini, A[i - 1][k])
        A[i][j] += mini

    return min(A[-1])
```


```
new Solution().minFallingPathSum()
```


---
**Score: 5**