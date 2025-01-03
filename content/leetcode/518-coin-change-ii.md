---
title: 518-Coin-Change-Ii
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/coin-change-ii


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
  def change(self, amount: int, coins: List[int]) -> int:
    dp = [1] + [0] * amount

    for coin in coins:
      for i in range(coin, amount + 1):
        dp[i] += dp[i - coin]

    return dp[amount]
```


```
new Solution().change()
```


---
**Score: 5**