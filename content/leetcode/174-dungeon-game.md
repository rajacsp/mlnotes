---
title: 174-Dungeon-Game
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/dungeon-game


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
  def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
    m = len(dungeon)
    n = len(dungeon[0])
    dp = [math.inf] * (n + 1)
    dp[n - 1] = 1

    for i in reversed(range(m)):
      for j in reversed(range(n)):
        dp[j] = min(dp[j], dp[j + 1]) - dungeon[i][j]
        dp[j] = max(dp[j], 1)

    return dp[0]
```


```
new Solution().calculateMinimumHP()
```


---
**Score: 5**