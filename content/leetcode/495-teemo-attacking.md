---
title: 495-Teemo-Attacking
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/teemo-attacking


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
  def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
    if duration == 0:
      return 0

    ans = 0

    for i in range(0, len(timeSeries) - 1):
      ans += min(timeSeries[i + 1] - timeSeries[i], duration)

    return ans + duration
```


```
new Solution().findPoisonedDuration()
```


---
**Score: 5**