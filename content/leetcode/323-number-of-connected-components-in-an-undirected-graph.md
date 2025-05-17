---
title: 323-Number-Of-Connected-Components-In-An-Undirected-Graph
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph


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
  def countComponents(self, n: int, edges: List[List[int]]) -> int:
    ans = 0
    graph = [[] for _ in range(n)]
    seen = set()

    for u, v in edges:
      graph[u].append(v)
      graph[v].append(u)

    def bfs(node: int, seen: Set[int]) -> None:
      q = deque([node])
      seen.add(node)

      while q:
        u = q.pop()
        for v in graph[u]:
          if v not in seen:
            q.append(v)
            seen.add(v)

    for i in range(n):
      if i not in seen:
        bfs(i, seen)
        ans += 1

    return ans
```


```
new Solution().countComponents()
```


---
**Score: 5**