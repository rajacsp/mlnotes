---
title: 711-Number-Of-Distinct-Islands-Ii
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/number-of-distinct-islands-ii


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
  def numDistinctIslands2(self, grid: List[List[int]]) -> int:
    seen = set()

    def dfs(i: int, j: int):
      if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]):
        return
      if grid[i][j] == 0 or (i, j) in seen:
        return

      seen.add((i, j))
      island.append((i, j))
      dfs(i + 1, j)
      dfs(i - 1, j)
      dfs(i, j + 1)
      dfs(i, j - 1)

    def normalize(island: List[tuple]) -> List[tuple]:
      # points[i] := 8 different rotations/reflections of island
      points = [[] for _ in range(8)]

      for i, j in island:
        points[0].append((i, j))
        points[1].append((i, -j))
        points[2].append((-i, j))
        points[3].append((-i, -j))
        points[4].append((j, i))
        points[5].append((j, -i))
        points[6].append((-j, i))
        points[7].append((-j, -i))

      points = [sorted(p) for p in points]

      # Normalize each p by minus p[1:] w/ p[0]
      for p in points:
        for i in range(1, len(island)):
          p[i] = (p[i][0] - p[0][0],
                  p[i][1] - p[0][1])
        p[0] = (0, 0)

      return sorted(points)[0]

    islands = set()  # All different shape islands

    for i in range(len(grid)):
      for j in range(len(grid[0])):
        island = []
        dfs(i, j)
        if island:
          islands.add(frozenset(normalize(island)))

    return len(islands)
```


```
new Solution().numDistinctIslands2()
```


---
**Score: 5**