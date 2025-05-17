---
title: 857-Minimum-Cost-To-Hire-K-Workers
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/minimum-cost-to-hire-k-workers


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
  def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
    ans = math.inf
    qualitySum = 0
    # (wagePerQuality, quality) sorted by wagePerQuality
    workers = sorted((w / q, q) for q, w in zip(quality, wage))
    maxHeap = []

    for wagePerQuality, q in workers:
      heapq.heappush(maxHeap, -q)
      qualitySum += q
      if len(maxHeap) > k:
        qualitySum += heapq.heappop(maxHeap)
      if len(maxHeap) == k:
        ans = min(ans, qualitySum * wagePerQuality)

    return ans
```


```
new Solution().mincostToHireWorkers()
```


---
**Score: 5**