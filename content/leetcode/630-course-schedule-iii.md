---
title: 630-Course-Schedule-Iii
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/course-schedule-iii


```python
import pyutil as pyu
pyu.get_local_pyinfo()
```


```python
print(pyu.ps2("python-dotenv"))
```


```python
from typing import List
```


```python
class Solution:
  def scheduleCourse(self, courses: List[List[int]]) -> int:
    time = 0
    maxHeap = []

    for duration, lastDay in sorted(courses, key=lambda x: x[1]):
      heapq.heappush(maxHeap, -duration)
      time += duration
      # If current course could not be taken, check if it's able to swap with a
      # Previously taken course with larger duration, to increase the time
      # Available to take upcoming courses
      if time > lastDay:
        time += heapq.heappop(maxHeap)

    return len(maxHeap)
```


```python
new Solution().scheduleCourse()
```


---
**Score: 5**