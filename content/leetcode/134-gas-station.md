---
title: 134-Gas-Station
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/gas-station


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
  def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    ans = 0
    net = 0
    summ = 0

    for i in range(len(gas)):
      net += gas[i] - cost[i]
      summ += gas[i] - cost[i]
      if summ < 0:
        summ = 0
        ans = i + 1

    return -1 if net < 0 else ans
```


```
new Solution().canCompleteCircuit()
```


---
**Score: 5**