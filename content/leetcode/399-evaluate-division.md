---
title: 399-Evaluate-Division
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/evaluate-division


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
  def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    ans = []
    # graph[A][B] := A / B
    graph = defaultdict(dict)

    for (A, B), value in zip(equations, values):
      graph[A][B] = value
      graph[B][A] = 1 / value

    # Returns A / C
    def devide(A: str, C: str, seen: Set[str]) -> float:
      if A == C:
        return 1.0

      seen.add(A)

      # Value := A / B
      for B, value in graph[A].items():
        if B in seen:
          continue
        res = devide(B, C, seen)  # B / C
        if res > 0:  # Valid
          return value * res  # (A / B) * (B / C) = A / C

      return -1.0  # Invalid

    for A, C in queries:
      if A not in graph and C not in graph:
        ans.append(-1.0)
      else:
        ans.append(devide(A, C, set()))

    return ans
```


```
new Solution().calcEquation()
```


---
**Score: 5**