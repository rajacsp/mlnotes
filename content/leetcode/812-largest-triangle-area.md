---
title: 812-Largest-Triangle-Area
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/largest-triangle-area


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
  def largestTriangleArea(self, points: List[List[int]]) -> float:
    ans = 0

    for Ax, Ay in points:
      for Bx, By in points:
        for Cx, Cy in points:
          ans = max(ans, 0.5 * abs((Bx - Ax) * (Cy - Ay) -
                                   (Cx - Ax) * (By - Ay)))

    return ans
```


```
new Solution().largestTriangleArea()
```


---
**Score: 5**