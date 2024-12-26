---
title: 807-Max-Increase-To-Keep-City-Skyline
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/max-increase-to-keep-city-skyline


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
  def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
    rowMax = list(map(max, grid))
    colMax = list(map(max, zip(*grid)))
    return sum(min(i, j) for i in rowMax for j in colMax) - sum(map(sum, grid))
```


```
new Solution().maxIncreaseKeepingSkyline()
```


---
**Score: 5**