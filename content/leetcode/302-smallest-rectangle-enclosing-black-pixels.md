---
title: 302-Smallest-Rectangle-Enclosing-Black-Pixels
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels


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
  def minArea(self, image: List[List[str]], x: int, y: int) -> int:
    m = len(image)
    n = len(image[0])
    dirs = [0, 1, 0, -1, 0]
    topLeft = [x, y]
    bottomRight = [x, y]
    q = deque([(x, y)])
    image[x][y] = '2'  # Visited

    while q:
      i, j = q.popleft()
      for k in range(4):
        r = i + dirs[k]
        c = j + dirs[k + 1]
        if r < 0 or r == m or c < 0 or c == n:
          continue
        if image[r][c] != '1':
          continue
        topLeft[0] = min(topLeft[0], r)
        topLeft[1] = min(topLeft[1], c)
        bottomRight[0] = max(bottomRight[0], r)
        bottomRight[1] = max(bottomRight[1], c)
        q.append((r, c))
        image[r][c] = '2'

    width = bottomRight[1] - topLeft[1] + 1
    height = bottomRight[0] - topLeft[0] + 1
    return width * height
```


```
new Solution().minArea()
```


---
**Score: 5**