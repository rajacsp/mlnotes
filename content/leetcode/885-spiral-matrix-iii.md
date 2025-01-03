---
title: 885-Spiral-Matrix-Iii
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/spiral-matrix-iii


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
  def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
    ans = [[r0, c0]]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    i = 0

    while len(ans) < R * C:
      for _ in range(i // 2 + 1):
        r0 += dy[i % 4]
        c0 += dx[i % 4]
        if 0 <= r0 < R and 0 <= c0 < C:
          ans.append([r0, c0])
      i += 1

    return ans
```


```
new Solution().spiralMatrixIII()
```


---
**Score: 5**