---
title: 986-Interval-List-Intersections
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/interval-list-intersections


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
  def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    ans = []
    i = 0
    j = 0

    while i < len(firstList) and j < len(secondList):
      # Lo := the start of the intersection
      # Hi := the end of the intersection
      lo = max(firstList[i][0], secondList[j][0])
      hi = min(firstList[i][1], secondList[j][1])
      if lo <= hi:
        ans.append([lo, hi])
      if firstList[i][1] < secondList[j][1]:
        i += 1
      else:
        j += 1

    return ans
```


```
new Solution().intervalIntersection()
```


---
**Score: 5**