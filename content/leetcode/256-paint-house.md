---
title: 256-Paint-House
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/paint-house


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
  def minCost(self, costs: List[List[int]]) -> List[List[int]]:
    for i in range(1, len(costs)):
      costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
      costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
      costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])

    return min(costs[-1])
```


```
new Solution().minCost()
```


---
**Score: 5**