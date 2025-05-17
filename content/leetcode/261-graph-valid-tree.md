---
title: 261-Graph-Valid-Tree
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/graph-valid-tree


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
  def validTree(self, n: int, edges: List[List[int]]) -> bool:
    if n == 0 or len(edges) != n - 1:
      return False

    graph = [[] for _ in range(n)]
    q = deque([0])
    seen = {0}

    for u, v in edges:
      graph[u].append(v)
      graph[v].append(u)

    while q:
      u = q.popleft()
      for v in graph[u]:
        if v not in seen:
          q.append(v)
          seen.add(v)

    return len(seen) == n
```


```
new Solution().validTree()
```


---
**Score: 5**