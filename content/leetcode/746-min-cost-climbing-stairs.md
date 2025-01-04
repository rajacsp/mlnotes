---
title: 746-Min-Cost-Climbing-Stairs
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/min-cost-climbing-stairs


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
  def minCostClimbingStairs(self, cost: List[int]) -> int:
    cost.append(0)

    for i in range(2, len(cost)):
      cost[i] += min(cost[i - 1], cost[i - 2])

    return cost[-1]
```


```
new Solution().minCostClimbingStairs()
```


---
**Score: 5**