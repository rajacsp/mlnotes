---
title: 790-Domino-And-Tromino-Tiling
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/domino-and-tromino-tiling


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
  def numTilings(self, N: int) -> int:
    kMod = 1_000_000_007
    dp = [0, 1, 2, 5] + [0] * 997

    for i in range(4, N + 1):
      dp[i] = 2 * dp[i - 1] + dp[i - 3]

    return dp[N] % kMod
```


```
new Solution().numTilings()
```


---
**Score: 5**