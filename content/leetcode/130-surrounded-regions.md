---
title: 130-Surrounded-Regions
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/surrounded-regions


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
  def solve(self, board: List[List[str]]) -> None:
    if not board:
      return

    m = len(board)
    n = len(board[0])
    dirs = [0, 1, 0, -1, 0]
    q = deque()

    for i in range(m):
      for j in range(n):
        if i * j == 0 or i == m - 1 or j == n - 1:
          if board[i][j] == 'O':
            q.append((i, j))
            board[i][j] = '*'

    # Mark grids that stretch from four sides with '*'
    while q:
      i, j = q.popleft()
      for k in range(4):
        x = i + dirs[k]
        y = j + dirs[k + 1]
        if x < 0 or x == m or y < 0 or y == n:
          continue
        if board[x][y] != 'O':
          continue
        q.append((x, y))
        board[x][y] = '*'

    for row in board:
      for i, c in enumerate(row):
        row[i] = 'O' if c == '*' else 'X'
```


```
new Solution().solve()
```


---
**Score: 5**