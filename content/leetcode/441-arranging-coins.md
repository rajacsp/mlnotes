---
title: 441-Arranging-Coins
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/arranging-coins


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
  def arrangeCoins(self, n: int) -> int:
    return int((-1 + sqrt(8 * n + 1)) // 2)
```


```
new Solution().arrangeCoins()
```


---
**Score: 5**