---
title: 309-Best-Time-To-Buy-And-Sell-Stock-With-Cooldown
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown


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
  def maxProfit(self, prices: List[int]) -> int:
    sell = 0
    hold = -math.inf
    prev = 0

    for price in prices:
      cache = sell
      sell = max(sell, hold + price)
      hold = max(hold, prev - price)
      prev = cache

    return sell
```


```
new Solution().maxProfit()
```


---
**Score: 5**