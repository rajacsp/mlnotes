---
title: 403-Frog-Jump
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/frog-jump


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
  def canCross(self, stones: List[int]) -> bool:
    n = len(stones)
    # dp[i][j] := True if a frog can make a size j jump to stones[i]
    dp = [[False] * (n + 1) for _ in range(n)]
    dp[0][0] = True

    for i in range(1, n):
      for j in range(i):
        k = stones[i] - stones[j]
        if k > n:
          continue
        for x in (k - 1, k, k + 1):
          if 0 <= x <= n:
            dp[i][k] |= dp[j][x]

    return any(dp[-1])
```


```
new Solution().canCross()
```


---
**Score: 5**