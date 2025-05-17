---
title: 122-Best-Time-To-Buy-And-Sell-Stock-Ii
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii


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

    for price in prices:
      sell = max(sell, hold + price)
      hold = max(hold, sell - price)

    return sell
```


```
new Solution().maxProfit()
```


---
**Score: 5**