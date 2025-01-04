---
title: 939-Minimum-Area-Rectangle
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/minimum-area-rectangle


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
  def minAreaRect(self, points: List[List[int]]) -> int:
    ans = math.inf
    xToYs = defaultdict(set)

    for x, y in points:
      xToYs[x].add(y)

    for i in range(len(points)):
      for j in range(i):
        x1, y1 = points[i]
        x2, y2 = points[j]
        if x1 == x2 or y1 == y2:
          continue
        if y2 in xToYs[x1] and y1 in xToYs[x2]:
          ans = min(ans, abs(x1 - x2) * abs(y1 - y2))

    return ans if ans < math.inf else 0
```


```
new Solution().minAreaRect()
```


---
**Score: 5**