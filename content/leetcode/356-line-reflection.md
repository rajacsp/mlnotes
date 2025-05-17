---
title: 356-Line-Reflection
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/line-reflection


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
  def isReflected(self, points: List[List[int]]) -> bool:
    minX = math.inf
    maxX = -math.inf
    seen = set()

    for x, y in points:
      minX = min(minX, x)
      maxX = max(maxX, x)
      seen.add((x, y))

    summ = minX + maxX
    # (leftX + rightX) / 2 = (minX + maxX) / 2
    #  leftX = minX + maxX - rightX
    # RightX = minX + maxX - leftX

    return all((summ - x, y) in seen for x, y in points)
```


```
new Solution().isReflected()
```


---
**Score: 5**