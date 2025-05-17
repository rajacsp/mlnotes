---
title: 279-Perfect-Squares
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/perfect-squares


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
  def numSquares(self, n: int) -> int:
    dp = [n] * (n + 1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
      j = 1
      while j * j <= i:
        dp[i] = min(dp[i], dp[i - j * j] + 1)
        j += 1

    return dp[n]
```


```
new Solution().numSquares()
```


---
**Score: 5**