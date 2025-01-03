---
title: 252-Meeting-Rooms
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/meeting-rooms


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
  def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
    intervals.sort()

    for i in range(1, len(intervals)):
      if intervals[i - 1][1] > intervals[i][0]:
        return False

    return True
```


```
new Solution().canAttendMeetings()
```


---
**Score: 5**