---
title: 861-Score-After-Flipping-Matrix
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/score-after-flipping-matrix


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
  def matrixScore(self, grid: List[List[int]]) -> int:
    # Flip rows with leading 0
    for row in grid:
      if row[0] == 0:
        self._flip(row)

    # Flip cols with 1s < 0s
    for j, col in enumerate(list(zip(*grid))):
      if sum(col) * 2 < len(grid):
        self._flipCol(grid, j)

    # Add binary number for each row
    return sum(self._binary(row) for row in grid)

  def _flip(self, row: List[int]) -> None:
    for i in range(len(row)):
      row[i] ^= 1

  def _flipCol(self, grid: List[List[int]], j: int) -> None:
    for i in range(len(grid)):
      grid[i][j] ^= 1

  def _binary(self, row: List[int]) -> int:
    res = row[0]
    for j in range(1, len(row)):
      res = res * 2 + row[j]
    return res
```


```
new Solution().matrixScore()
```


---
**Score: 5**