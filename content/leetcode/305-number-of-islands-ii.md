---
title: 305-Number-Of-Islands-Ii
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/number-of-islands-ii


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
    self.id = [-1] * n

  def union(self, u: int, v: int) -> None:
    self.id[u] = v

  def find(self, u: int) -> int:
    if self.id[u] != u:
      self.id[u] = self.find(self.id[u])
    return self.id[u]


class Solution:
  def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
    dirs = [0, 1, 0, -1, 0]
    ans = []
    seen = [[False] * n for _ in range(m)]
    uf = UnionFind(m * n)
    count = 0

    def getId(i: int, j: int, n: int) -> int:
      return i * n + j

    for i, j in positions:
      if seen[i][j]:
        ans.append(count)
        continue
      seen[i][j] = True
      id = getId(i, j, n)
      uf.id[id] = id
      count += 1
      for k in range(4):
        x = i + dirs[k]
        y = j + dirs[k + 1]
        if x < 0 or x == m or y < 0 or y == n:
          continue
        neighborId = getId(x, y, n)
        if uf.id[neighborId] == -1:  # Water
          continue
        currentParent = uf.find(id)
        neighborParent = uf.find(neighborId)
        if currentParent != neighborParent:
          uf.union(currentParent, neighborParent)
          count -= 1
      ans.append(count)

    return ans
```


```
new Solution().numIslands2()
```


---
**Score: 5**