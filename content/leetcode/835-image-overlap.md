---
title: 835-Image-Overlap
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/image-overlap


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
  def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
    n = len(A)
    magic = 100
    onesA = []
    onesB = []
    dict = defaultdict(int)

    for i in range(n):
      for j in range(n):
        if A[i][j] == 1:
          onesA.append([i, j])
        if B[i][j] == 1:
          onesB.append([i, j])

    for a in onesA:
      for b in onesB:
        dict[(a[0] - b[0]) * magic + (a[1] - b[1])] += 1

    return max(dict.values()) if dict else 0
```


```
new Solution().largestOverlap()
```


---
**Score: 5**