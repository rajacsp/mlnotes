---
title: 70-Climbing-Stairs
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/climbing-stairs


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
  def climbStairs(self, n: int) -> int:
    # dp[i] := # Of distinct ways to climb to i-th stair
    dp = [1, 1] + [0] * (n - 1)

    for i in range(2, n + 1):
      dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
```


```
new Solution().climbStairs()
```


---
**Score: 5**