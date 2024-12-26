---
title: 1058-Minimize-Rounding-Error-To-Meet-Target
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/minimize-rounding-error-to-meet-target


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
  def minimizeError(self, prices: List[str], target: int) -> str:
    # A[i] := (costCeil - costFloor, costCeil, costFloor)
    # The lower the costCeil - costFloor, the cheaper to ceil it
    A = []
    sumFloored = 0
    sumCeiled = 0

    for price in map(float, prices):
      floored = math.floor(price)
      ceiled = math.ceil(price)
      sumFloored += floored
      sumCeiled += ceiled
      costFloor = price - floored
      costCeil = ceiled - price
      A.append((costCeil - costFloor, costCeil, costFloor))

    if not sumFloored <= target <= sumCeiled:
      return '-1'

    A.sort()
    nCeiled = target - sumFloored
    return '{:.3f}'.format(sum(a[1] for a in A[:nCeiled]) +
                           sum(a[2] for a in A[nCeiled:]))
```


```
new Solution().minimizeError()
```


---
**Score: 5**