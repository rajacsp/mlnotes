---
title: 547-Number-Of-Provinces
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/number-of-provinces


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
    self.count = n
    self.id = list(range(n))

  def union(self, u: int, v: int) -> None:
    i = self.find(u)
    j = self.find(v)
    if i == j:
      return
    self.id[i] = j
    self.count -= 1

  def find(self, u: int) -> int:
    if self.id[u] != u:
      self.id[u] = self.find(self.id[u])
    return self.id[u]


class Solution:
  def findCircleNum(self, M: List[List[int]]) -> int:
    n = len(M)
    uf = UnionFind(n)

    for i in range(n):
      for j in range(i, n):
        if M[i][j] == 1:
          uf.union(i, j)

    return uf.count
```


```
new Solution().findCircleNum()
```


---
**Score: 5**