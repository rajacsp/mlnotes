---
title: 877-Stone-Game
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/stone-game


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
  def stoneGame(self, piles: List[int]) -> bool:
    n = len(piles)
    # dp[i][j] := max stones you can get more than your opponent in piles[i..j]
    dp = [[0] * n for _ in range(n)]

    for i, pile in enumerate(piles):
      dp[i][i] = pile

    for d in range(1, n):
      for i in range(n - d):
        j = i + d
        dp[i][j] = max(piles[i] - dp[i + 1][j],
                       piles[j] - dp[i][j - 1])

    return dp[0][n - 1] > 0
```


```
new Solution().stoneGame()
```


---
**Score: 5**