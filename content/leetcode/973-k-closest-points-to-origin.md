---
title: 973-K-Closest-Points-To-Origin
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/k-closest-points-to-origin


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
  def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    maxHeap = []

    for x, y in points:
      heapq.heappush(maxHeap, (- x * x - y * y, [x, y]))
      if len(maxHeap) > K:
        heapq.heappop(maxHeap)

    return [pair[1] for pair in maxHeap]
```


```
new Solution().kClosest()
```


---
**Score: 5**