---
title: 253-Meeting-Rooms-Ii
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/meeting-rooms-ii


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
  def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    minHeap = []  # Store end times of each room

    for start, end in sorted(intervals):
      if minHeap and start >= minHeap[0]:
        heapq.heappop(minHeap)
      heapq.heappush(minHeap, end)

    return len(minHeap)
```


```
new Solution().minMeetingRooms()
```


---
**Score: 5**