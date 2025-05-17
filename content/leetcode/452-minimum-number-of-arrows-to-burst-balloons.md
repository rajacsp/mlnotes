---
title: 452-Minimum-Number-Of-Arrows-To-Burst-Balloons
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons


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
  def findMinArrowShots(self, points: List[List[int]]) -> int:
    ans = 0
    arrowX = -math.inf

    for point in sorted(points, key=lambda x: x[1]):
      if point[0] > arrowX:
        ans += 1
        arrowX = point[1]

    return ans
```


```
new Solution().findMinArrowShots()
```


---
**Score: 5**