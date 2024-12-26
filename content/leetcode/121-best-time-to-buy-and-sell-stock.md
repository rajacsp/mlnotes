---
title: 121-Best-Time-To-Buy-And-Sell-Stock
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/best-time-to-buy-and-sell-stock


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
    sellOne = 0
    holdOne = -math.inf

    for price in prices:
      sellOne = max(sellOne, holdOne + price)
      holdOne = max(holdOne, -price)

    return sellOne
```


```
new Solution().maxProfit()
```


---
**Score: 5**