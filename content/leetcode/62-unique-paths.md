---
title: 62-Unique-Paths
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/unique-paths


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
  def uniquePaths(self, m: int, n: int) -> int:
    # dp[i][j] := unique paths from (0, 0) to (i, j)
    dp = [[1] * n for _ in range(m)]

    for i in range(1, m):
      for j in range(1, n):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]
```


```
new Solution().uniquePaths()
```


---
**Score: 5**