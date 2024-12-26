---
title: 539-Minimum-Time-Difference
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/minimum-time-difference


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
  def findMinDifference(self, timePoints: List[str]) -> int:
    ans = 24 * 60
    nums = sorted([int(timePoint[:2]) * 60 + int(timePoint[3:])
                   for timePoint in timePoints])

    for a, b in zip(nums, nums[1:]):
      ans = min(ans, b - a)

    return min(ans, 24 * 60 - nums[-1] + nums[0])
```


```
new Solution().findMinDifference()
```


---
**Score: 5**