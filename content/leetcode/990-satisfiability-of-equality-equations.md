---
title: 990-Satisfiability-Of-Equality-Equations
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/satisfiability-of-equality-equations


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
class UnionFind:
  def __init__(self, n: int):
    self.id = list(range(n))

  def union(self, u: int, v: int) -> None:
    self.id[self.find(u)] = self.find(v)

  def find(self, u: int) -> int:
    if self.id[u] != u:
      self.id[u] = self.find(self.id[u])
    return self.id[u]


class Solution:
  def equationsPossible(self, equations: List[str]) -> bool:
    uf = UnionFind(26)

    for x, op, _, y in equations:
      if op == '=':
        uf.union(ord(x) - ord('a'), ord(y) - ord('a'))

    return all(uf.find(ord(x) - ord('a')) != uf.find(ord(y) - ord('a'))
               for x, op, _, y in equations
               if op == '!')
```


```
new Solution().equationsPossible()
```


---
**Score: 5**