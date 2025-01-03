---
title: 310-Minimum-Height-Trees
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/minimum-height-trees


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
  def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    if n == 1 or not edges:
      return [0]

    ans = []
    graph = defaultdict(set)

    for u, v in edges:
      graph[u].add(v)
      graph[v].add(u)

    for label, children in graph.items():
      if len(children) == 1:
        ans.append(label)

    while n > 2:
      n -= len(ans)
      nextLeaves = []
      for leaf in ans:
        u = next(iter(graph[leaf]))
        graph[u].remove(leaf)
        if len(graph[u]) == 1:
          nextLeaves.append(u)
      ans = nextLeaves

    return ans
```


```
new Solution().findMinHeightTrees()
```


---
**Score: 5**