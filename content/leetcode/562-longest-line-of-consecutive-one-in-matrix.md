---
title: 562-Longest-Line-Of-Consecutive-One-In-Matrix
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix


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
  def longestLine(self, mat: List[List[int]]) -> int:
    m = len(mat)
    n = len(mat[0])
    ans = 0
    # dp[i][j][0] := horizontal
    # dp[i][j][1] := vertical
    # dp[i][j][2] := diagonal
    # dp[i][j][3] := anti-diagonal
    dp = [[[0] * 4 for j in range(n)] for _ in range(m)]

    for i in range(m):
      for j in range(n):
        if mat[i][j] == 1:
          dp[i][j][0] = dp[i][j - 1][0] + 1 if j > 0 else 1
          dp[i][j][1] = dp[i - 1][j][1] + 1 if i > 0 else 1
          dp[i][j][2] = dp[i - 1][j - 1][2] + 1 if i > 0 and j > 0 else 1
          dp[i][j][3] = dp[i - 1][j + 1][3] + 1 if i > 0 and j < n - 1 else 1
          ans = max(ans, max(dp[i][j]))

    return ans
```


```
new Solution().longestLine()
```


---
**Score: 5**