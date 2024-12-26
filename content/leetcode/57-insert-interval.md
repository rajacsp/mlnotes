---
title: 57-Insert-Interval
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/insert-interval


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
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    n = len(intervals)
    ans = []
    i = 0

    while i < n and intervals[i][1] < newInterval[0]:
      ans.append(intervals[i])
      i += 1

    while i < n and intervals[i][0] <= newInterval[1]:
      newInterval[0] = min(newInterval[0], intervals[i][0])
      newInterval[1] = max(newInterval[1], intervals[i][1])
      i += 1

    ans.append(newInterval)

    while i < n:
      ans.append(intervals[i])
      i += 1

    return ans
```


```
new Solution().insert()
```


---
**Score: 5**