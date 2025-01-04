---
title: 207-Course-Schedule
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/course-schedule


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
from enum import Enum


class State(Enum):
  kInit = 0
  kVisiting = 1
  kVisited = 2


class Solution:
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = [[] for _ in range(numCourses)]
    state = [State.kInit] * numCourses

    for a, b in prerequisites:
      graph[b].append(a)

    def hasCycle(u: int) -> bool:
      if state[u] == State.kVisiting:
        return True
      if state[u] == State.kVisited:
        return False

      state[u] = State.kVisiting
      if any(hasCycle(v) for v in graph[u]):
        return True
      state[u] = State.kVisited

      return False

    return not any(hasCycle(i) for i in range(numCourses))
```


```
new Solution().canFinish()
```


---
**Score: 5**