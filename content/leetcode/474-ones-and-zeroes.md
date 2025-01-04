---
title: 474-Ones-And-Zeroes
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/ones-and-zeroes


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
  def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
    # dp[i][j] := max size of the subset given i 0's and j 1's are available
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for s in strs:
      count0 = s.count('0')
      count1 = len(s) - count0
      for i in range(m, count0 - 1, -1):
        for j in range(n, count1 - 1, -1):
          dp[i][j] = max(dp[i][j], dp[i - count0][j - count1] + 1)

    return dp[m][n]
```


```
new Solution().findMaxForm()
```


---
**Score: 5**