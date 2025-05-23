---
title: 1057-Campus-Bikes
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/campus-bikes


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
  def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
    ans = [-1] * len(workers)
    usedBikes = [False] * len(bikes)
    # buckets[k] := (i, j), where k = dist(workers[i], bikes[j])
    buckets = [[] for _ in range(2001)]

    def dist(p1: List[int], p2: List[int]) -> int:
      return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    for i, worker in enumerate(workers):
      for j, bike in enumerate(bikes):
        buckets[dist(worker, bike)].append((i, j))

    for k in range(2001):
      for i, j in buckets[k]:
        if ans[i] == -1 and not usedBikes[j]:
          ans[i] = j
          usedBikes[j] = True

    return ans
```


```
new Solution().assignBikes()
```


---
**Score: 5**