---
title: 329-Longest-Increasing-Path-In-A-Matrix
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/longest-increasing-path-in-a-matrix


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
  def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    m = len(matrix)
    n = len(matrix[0])

    @functools.lru_cache(None)
    def dfs(i: int, j: int, prev: int) -> int:
      if i < 0 or i == m or j < 0 or j == n:
        return 0
      if matrix[i][j] <= prev:
        return 0

      curr = matrix[i][j]
      return 1 + max(dfs(i + 1, j, curr),
                     dfs(i - 1, j, curr),
                     dfs(i, j + 1, curr),
                     dfs(i, j - 1, curr))

    return max(dfs(i, j, -math.inf) for i in range(m) for j in range(n))
```


```
new Solution().longestIncreasingPath()
```


---
**Score: 5**