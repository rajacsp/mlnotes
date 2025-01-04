---
title: 851-Loud-And-Rich
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/loud-and-rich


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
  def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
    graph = [[] for _ in range(len(quiet))]

    for u, v in richer:
      graph[v].append(u)

    @functools.lru_cache(None)
    def dfs(u: int) -> int:
      ans = u

      for v in graph[u]:
        res = dfs(v)
        if quiet[res] < quiet[ans]:
          ans = res

      return ans

    return map(dfs, range(len(graph)))
```


```
new Solution().loudAndRich()
```


---
**Score: 5**