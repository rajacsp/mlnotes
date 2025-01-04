---
title: 463-Island-Perimeter
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/island-perimeter


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
  def islandPerimeter(self, grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])

    islands = 0
    neighbors = 0

    for i in range(m):
      for j in range(n):
        if grid[i][j] == 1:
          islands += 1
          if i + 1 < m and grid[i + 1][j] == 1:
            neighbors += 1
          if j + 1 < n and grid[i][j + 1] == 1:
            neighbors += 1

    return islands * 4 - neighbors * 2
```


```
new Solution().islandPerimeter()
```


---
**Score: 5**