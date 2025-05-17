---
title: 847-Shortest-Path-Visiting-All-Nodes
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/shortest-path-visiting-all-nodes


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
  def shortestPathLength(self, graph: List[List[int]]) -> int:
    n = len(graph)
    goal = (1 << n) - 1

    ans = 0
    q = deque()  # (u, state)
    seen = set()

    for i in range(n):
      q.append((i, 1 << i))

    while q:
      for _ in range(len(q)):
        u, state = q.popleft()
        if state == goal:
          return ans
        if (u, state) in seen:
          continue
        seen.add((u, state))
        for v in graph[u]:
          q.append((v, state | (1 << v)))
      ans += 1

    return -1
```


```
new Solution().shortestPathLength()
```


---
**Score: 5**