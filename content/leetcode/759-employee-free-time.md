---
title: 759-Employee-Free-Time
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/employee-free-time


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
  def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
    ans = []
    intervals = []

    for s in schedule:
      intervals.extend(s)

    intervals.sort(key=lambda x: x.start)

    prevEnd = intervals[0].end

    for interval in intervals:
      if interval.start > prevEnd:
        ans.append(Interval(prevEnd, interval.start))
      prevEnd = max(prevEnd, interval.end)

    return ans
```


```
new Solution().employeeFreeTime()
```


---
**Score: 5**