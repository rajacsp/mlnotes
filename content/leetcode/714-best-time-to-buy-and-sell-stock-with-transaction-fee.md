---
title: 714-Best-Time-To-Buy-And-Sell-Stock-With-Transaction-Fee
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee


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
  def maxProfit(self, prices: List[int], fee: int) -> int:
    sell = 0
    hold = -math.inf

    for price in prices:
      sell = max(sell, hold + price)
      hold = max(hold, sell - price - fee)

    return sell
```


```
new Solution().maxProfit()
```


---
**Score: 5**