---
title: 200-Number-Of-Islands
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/number-of-islands


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
  def numIslands(self, grid: List[List[str]]) -> int:
    m = len(grid)
    n = len(grid[0])
    dirs = [0, 1, 0, -1, 0]

    def bfs(r, c):
      q = deque([(r, c)])
      grid[r][c] = '2'  # Mark '2' as visited
      while q:
        i, j = q.popleft()
        for k in range(4):
          x = i + dirs[k]
          y = j + dirs[k + 1]
          if x < 0 or x == m or y < 0 or y == n:
            continue
          if grid[x][y] != '1':
            continue
          q.append((x, y))
          grid[x][y] = '2'  # Mark '2' as visited

    ans = 0

    for i in range(m):
      for j in range(n):
        if grid[i][j] == '1':
          bfs(i, j)
          ans += 1

    return ans
```


```
new Solution().numIslands()
```


---
**Score: 5**