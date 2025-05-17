---
title: 870-Advantage-Shuffle
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/advantage-shuffle


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
from sortedcontainers import SortedList


class Solution:
  def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
    sl = SortedList(A)

    for i, b in enumerate(B):
      index = 0 if sl[-1] <= b else sl.bisect_right(b)
      A[i] = sl[index]
      del sl[index]

    return A
```


```
new Solution().advantageCount()
```


---
**Score: 5**