---
title: 766-Toeplitz-Matrix
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/toeplitz-matrix


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
  def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
    for i in range(len(matrix) - 1):
      for j in range(len(matrix[0]) - 1):
        if matrix[i][j] != matrix[i + 1][j + 1]:
          return False

    return True
```


```
new Solution().isToeplitzMatrix()
```


---
**Score: 5**