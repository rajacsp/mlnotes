---
title: 915-Partition-Array-Into-Disjoint-Intervals
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/partition-array-into-disjoint-intervals


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
  def partitionDisjoint(self, A: List[int]) -> int:
    n = len(A)
    mini = [0] * (n - 1) + [A[-1]]
    maxi = -math.inf

    for i in range(n - 2, - 1, -1):
      mini[i] = min(mini[i + 1], A[i])

    for i, a in enumerate(A):
      maxi = max(maxi, a)
      if maxi <= mini[i + 1]:
        return i + 1
```


```
new Solution().partitionDisjoint()
```


---
**Score: 5**