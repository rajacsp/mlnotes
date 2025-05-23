---
title: 935-Knight-Dialer
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/knight-dialer


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
  def knightDialer(self, n: int) -> int:
    kMod = 1_000_000_007
    dirs = [(-2, 1), (-1, 2), (1, 2), (2, 1),
            (2, -1), (1, -2), (-1, -2), (-2, -1)]

    # dp[i][j] := # Of ways stand on (i, j)
    dp = [[1] * 3 for _ in range(4)]
    dp[3][0] = dp[3][2] = 0

    for _ in range(n - 1):
      newDp = [[0] * 3 for _ in range(4)]
      for i in range(4):
        for j in range(3):
          if (i, j) in ((3, 0), (3, 2)):
            continue
          for dx, dy in dirs:
            x = i + dx
            y = j + dy
            if x < 0 or x >= 4 or y < 0 or y >= 3:
              continue
            if (x, y) in ((3, 0), (3, 2)):
              continue
            newDp[x][y] = (newDp[x][y] + dp[i][j]) % kMod
      dp = newDp

    return sum(map(sum, dp)) % kMod
```


```
new Solution().knightDialer()
```


---
**Score: 5**