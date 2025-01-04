---
title: 490-The-Maze
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/the-maze


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
  def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
    m = len(maze)
    n = len(maze[0])
    dirs = [0, 1, 0, -1, 0]
    q = deque([(start[0], start[1])])
    seen = {(start[0], start[1])}

    def isValid(x: int, y: int) -> bool:
      return 0 <= x < m and 0 <= y < n and maze[x][y] == 0

    while q:
      i, j = q.popleft()
      for k in range(4):
        x = i
        y = j
        while isValid(x + dirs[k], y + dirs[k + 1]):
          x += dirs[k]
          y += dirs[k + 1]
        if [x, y] == destination:
          return True
        if (x, y) in seen:
          continue
        q.append((x, y))
        seen.add((x, y))

    return False
```


```
new Solution().hasPath()
```


---
**Score: 5**