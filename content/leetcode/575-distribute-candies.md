---
title: 575-Distribute-Candies
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/distribute-candies


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
  def distributeCandies(self, candies: List[int]) -> int:
    return min(len(candies) // 2, len(set(candies)))
```


```
new Solution().distributeCandies()
```


---
**Score: 5**