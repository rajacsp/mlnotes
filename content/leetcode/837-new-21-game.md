---
title: 837-New-21-Game
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/new-21-game


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
  def new21Game(self, n: int, k: int, maxPts: int) -> float:
    # When the game ends, the point is in [k..k - 1 + maxPts]
    #   P = 1, if n >= k - 1 + maxPts
    #   P = 0, if n < k (note the constraints already have k <= n)
    if k == 0 or n >= k - 1 + maxPts:
      return 1.0

    ans = 0.0
    dp = [1.0] + [0] * n  # dp[i] := prob to have i points
    windowSum = dp[0]  # P(i - 1) + P(i - 2) + ... + P(i - maxPts)

    for i in range(1, n + 1):
      # The prob to get point i is
      # P(i) = [P(i - 1) + P(i - 2) + ... + P(i - maxPts)] / maxPts
      dp[i] = windowSum / maxPts
      if i < k:
        windowSum += dp[i]
      else:  # The game ends
        ans += dp[i]
      if i - maxPts >= 0:
        windowSum -= dp[i - maxPts]

    return ans
```


```
new Solution().new21Game()
```


---
**Score: 5**