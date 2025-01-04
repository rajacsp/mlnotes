---
title: 276-Paint-Fence
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/paint-fence


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
  def numWays(self, n: int, k: int) -> int:
    if n == 0:
      return 0
    if n == 1:
      return k
    if n == 2:
      return k * k

    # dp[i] := # Of ways to pan posts with k colors
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = k
    dp[2] = k * k

    for i in range(3, n + 1):
      dp[i] = (dp[i - 1] + dp[i - 2]) * (k - 1)

    return dp[n]
```


```
new Solution().numWays()
```


---
**Score: 5**