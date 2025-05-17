---
title: 1040-Moving-Stones-Until-Consecutive-Ii
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/moving-stones-until-consecutive-ii


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
  def numMovesStonesII(self, stones: List[int]) -> List[int]:
    n = len(stones)
    minMoves = n

    stones.sort()

    l = 0
    for r, stone in enumerate(stones):
      while stone - stones[l] + 1 > n:
        l += 1
      alreadyStored = r - l + 1
      if alreadyStored == n - 1 and stone - stones[l] + 1 == n - 1:
        minMoves = 2
      else:
        minMoves = min(minMoves, n - alreadyStored)

    return [minMoves, max(stones[n - 1] - stones[1] - n + 2, stones[n - 2] - stones[0] - n + 2)]
```


```
new Solution().numMovesStonesII()
```


---
**Score: 5**