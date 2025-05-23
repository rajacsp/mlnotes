---
title: 473-Matchsticks-To-Square
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/matchsticks-to-square


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
  def makesquare(self, matchsticks: List[int]) -> bool:
    if len(matchsticks) < 4:
      return False

    perimeter = sum(matchsticks)
    if perimeter % 4 != 0:
      return False

    A = sorted(matchsticks)[::-1]

    def dfs(selected: int, edges: List[int]) -> bool:
      if selected == len(A):
        return all(edge == edges[0] for edge in edges)

      for i, edge in enumerate(edges):
        if A[selected] > edge:
          continue
        edges[i] -= A[selected]
        if dfs(selected + 1, edges):
          return True
        edges[i] += A[selected]

      return False

    return dfs(0, [perimeter // 4] * 4)
```


```
new Solution().makesquare()
```


---
**Score: 5**