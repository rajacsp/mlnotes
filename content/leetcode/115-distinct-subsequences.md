---
title: 115-Distinct-Subsequences
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/distinct-subsequences


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
  def numDistinct(self, s: str, t: str) -> int:
    m = len(s)
    n = len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
      dp[i][0] = 1

    for i in range(1, m + 1):
      for j in range(1, n + 1):
        if s[i - 1] == t[j - 1]:
          dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        else:
          dp[i][j] = dp[i - 1][j]

    return dp[m][n]
```


```
new Solution().numDistinct()
```


---
**Score: 5**