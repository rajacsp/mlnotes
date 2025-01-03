---
title: 1034-Coloring-A-Border
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/coloring-a-border


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
  def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
    def dfs(i: int, j: int, originalColor: int) -> None:
      if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] != originalColor:
        return

      grid[i][j] = -originalColor
      dfs(i + 1, j, originalColor)
      dfs(i - 1, j, originalColor)
      dfs(i, j + 1, originalColor)
      dfs(i, j - 1, originalColor)

      if 0 < i < len(grid) - 1 and 0 < j < len(grid[0]) - 1 and \
              abs(grid[i + 1][j]) == originalColor and \
              abs(grid[i - 1][j]) == originalColor and \
              abs(grid[i][j + 1]) == originalColor and \
              abs(grid[i][j - 1]) == originalColor:
        grid[i][j] = originalColor

    dfs(r0, c0, grid[r0][c0])

    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] < 0:
          grid[i][j] = color

    return grid
```


```
new Solution().colorBorder()
```


---
**Score: 5**