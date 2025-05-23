---
title: 952-Largest-Component-Size-By-Common-Factor
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/largest-component-size-by-common-factor


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
    self.id = [i for i in range(n + 1)]

  def union(self, u: int, v: int) -> bool:
    i = self.find(u)
    j = self.find(v)
    if i == j:
      return False
    self.id[i] = j
    return True

  def find(self, u: int) -> int:
    if self.id[u] != u:
      self.id[u] = self.find(self.id[u])
    return self.id[u]


class Solution:
  def largestComponentSize(self, A: List[int]) -> int:
    ans = 0
    uf = UnionFind(max(A))
    count = Counter()

    for a in A:
      for num in range(2, int(sqrt(a) + 1)):
        if a % num == 0:
          uf.union(a, num)
          uf.union(a, a // num)

    for a in A:
      pa = uf.find(a)
      count[pa] += 1
      ans = max(ans, count[pa])

    return ans
```


```
new Solution().largestComponentSize()
```


---
**Score: 5**