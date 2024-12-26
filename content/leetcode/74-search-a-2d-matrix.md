---
title: 74-Search-A-2D-Matrix
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/search-a-2d-matrix


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
    if not matrix:
      return False

    m = len(matrix)
    n = len(matrix[0])
    l = 0
    r = m * n

    while l < r:
      mid = (l + r) // 2
      i = mid // n
      j = mid % n
      if matrix[i][j] == target:
        return True
      if matrix[i][j] < target:
        l = mid + 1
      else:
        r = mid

    return False
```


```
new Solution().searchMatrix()
```


---
**Score: 5**