---
title: 1029-Two-City-Scheduling
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/two-city-scheduling


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
  def twoCitySchedCost(self, costs: List[List[int]]) -> int:
    n = len(costs) // 2

    # How much money can we save if we fly a person to A instead of B?
    # To save money, we should
    #   1) fly the person with the max saving to A
    #   2) fly the person with the min saving to B

    # Sort in descending order by the money saved if we fly a person to A
    costs.sort(key=lambda x: x[0] - x[1])
    return sum(costs[i][0] + costs[i + n][1] for i in range(n))
```


```
new Solution().twoCitySchedCost()
```


---
**Score: 5**