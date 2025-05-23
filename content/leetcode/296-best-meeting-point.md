---
title: 296-Best-Meeting-Point
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/best-meeting-point


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
  def minTotalDistance(self, grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    # I indices s.t. grid[i][j] == 1
    I = [i for i in range(m) for j in range(n) if grid[i][j]]
    # J indices s.t. grid[i][j] == 1
    J = [j for j in range(n) for i in range(m) if grid[i][j]]

    def minTotalDistance(grid: List[int]) -> int:
      summ = 0
      i = 0
      j = len(grid) - 1

      while i < j:
        summ += grid[j] - grid[i]
        i += 1
        j -= 1

      return summ

    # Sum(i - median(I)) + sum(j - median(J))
    return minTotalDistance(I) + minTotalDistance(J)
```


```
new Solution().minTotalDistance()
```


---
**Score: 5**