---
title: 517-Super-Washing-Machines
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/super-washing-machines


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
  def findMinMoves(self, machines: List[int]) -> int:
    dresses = sum(machines)

    if dresses % len(machines) != 0:
      return -1

    ans = 0
    average = dresses // len(machines)
    inout = 0

    for dress in machines:
      inout += dress - average
      ans = max(ans, abs(inout), dress - average)

    return ans
```


```
new Solution().findMinMoves()
```


---
**Score: 5**