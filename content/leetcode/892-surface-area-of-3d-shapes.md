---
title: 892-Surface-Area-Of-3D-Shapes
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/surface-area-of-3d-shapes


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
  def surfaceArea(self, grid: List[List[int]]) -> int:
    ans = 0

    for i in range(len(grid)):
      for j in range(len(grid)):
        if grid[i][j]:
          ans += grid[i][j] * 4 + 2
        if i > 0:
          ans -= min(grid[i][j], grid[i - 1][j]) * 2
        if j > 0:
          ans -= min(grid[i][j], grid[i][j - 1]) * 2

    return ans
```


```
new Solution().surfaceArea()
```


---
**Score: 5**