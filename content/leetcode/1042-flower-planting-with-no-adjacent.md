---
title: 1042-Flower-Planting-With-No-Adjacent
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/flower-planting-with-no-adjacent


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
  def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
    ans = [0] * n  # ans[i] := 1, 2, 3, or 4
    graph = [[] for _ in range(n)]

    for a, b in paths:
      u = a - 1
      v = b - 1
      graph[u].append(v)
      graph[v].append(u)

    for i in range(n):
      used = [False] * 5
      for v in graph[i]:
        used[ans[v]] = True
      for type in range(1, 5):
        if not used[type]:
          ans[i] = type
          break

    return ans
```


```
new Solution().gardenNoAdj()
```


---
**Score: 5**