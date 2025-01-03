---
title: 1049-Last-Stone-Weight-Ii
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/last-stone-weight-ii


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
  def lastStoneWeightII(self, stones: List[int]) -> int:
    summ = sum(stones)
    s = 0
    dp = [True] + [False] * summ

    for stone in stones:
      for w in range(summ // 2 + 1)[::-1]:
        if w >= stone:
          dp[w] = dp[w] or dp[w - stone]
        if dp[w]:
          s = max(s, w)

    return summ - 2 * s
```


```
new Solution().lastStoneWeightII()
```


---
**Score: 5**