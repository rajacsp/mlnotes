---
title: 123-Best-Time-To-Buy-And-Sell-Stock-Iii
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii


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
    sellTwo = 0
    holdTwo = -math.inf
    sellOne = 0
    holdOne = -math.inf

    for price in prices:
      sellTwo = max(sellTwo, holdTwo + price)
      holdTwo = max(holdTwo, sellOne - price)
      sellOne = max(sellOne, holdOne + price)
      holdOne = max(holdOne, -price)

    return sellTwo
```


```
new Solution().maxProfit()
```


---
**Score: 5**