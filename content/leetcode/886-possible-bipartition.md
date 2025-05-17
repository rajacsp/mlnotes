---
title: 886-Possible-Bipartition
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/possible-bipartition


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


class Color(Enum):
  kWhite = 0
  kRed = 1
  kGreen = 2


class Solution:
  def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
    graph = [[] for _ in range(n + 1)]
    colors = [Color.kWhite] * (n + 1)

    for u, v in dislikes:
      graph[u].append(v)
      graph[v].append(u)

    # Reduce to 785. Is Graph Bipartite?
    def isValidColor(u: int, color: Color) -> bool:
      # The painted color should be same as the `color`
      if colors[u] != Color.kWhite:
        return colors[u] == color

      colors[u] = color  # Always paint w/ `color`

      # All children should have valid colors
      childrenColor = Color.kRed if colors[u] == Color.kGreen else Color.kGreen
      return all(isValidColor(v, childrenColor) for v in graph[u])

    return all(colors[i] != Color.kWhite or isValidColor(i, Color.kRed)
               for i in range(1, n + 1))
```


```
new Solution().possibleBipartition()
```


---
**Score: 5**