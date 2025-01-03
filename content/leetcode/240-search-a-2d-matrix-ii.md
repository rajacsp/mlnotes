---
title: 240-Search-A-2D-Matrix-Ii
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/search-a-2d-matrix-ii


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
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    r = 0
    c = len(matrix[0]) - 1

    while r < len(matrix) and c >= 0:
      if matrix[r][c] == target:
        return True
      if target < matrix[r][c]:
        c -= 1
      else:
        r += 1

    return False
```


```
new Solution().searchMatrix()
```


---
**Score: 5**