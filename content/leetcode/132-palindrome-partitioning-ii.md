---
title: 132-Palindrome-Partitioning-Ii
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/palindrome-partitioning-ii


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
  def minCut(self, s: str) -> int:
    n = len(s)
    cut = [0] * n
    dp = [[False] * n for _ in range(n)]

    for i in range(n):
      mini = i
      for j in range(i + 1):
        if s[j] == s[i] and (j + 1 > i - 1 or dp[j + 1][i - 1]):
          dp[j][i] = True
          mini = 0 if j == 0 else min(mini, cut[j - 1] + 1)
      cut[i] = mini

    return cut[n - 1]
```


```
new Solution().minCut()
```


---
**Score: 5**