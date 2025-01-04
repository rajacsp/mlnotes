---
title: 853-Car-Fleet
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/car-fleet


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
  def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    ans = 0
    times = [
        float(target - p) / s for p, s in sorted(zip(position, speed),
                                                 reverse=True)]
    maxTime = 0  # The time of the slowest car to reach the target

    for time in times:
      # A car needs more time to reach the target, so it becomes slowest
      if time > maxTime:
        maxTime = time
        ans += 1

    return ans
```


```
new Solution().carFleet()
```


---
**Score: 5**