---
title: 73-Set-Matrix-Zeroes
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/set-matrix-zeroes


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
  def setZeroes(self, matrix: List[List[int]]) -> None:
    m = len(matrix)
    n = len(matrix[0])
    shouldFillFirstRow = 0 in matrix[0]
    shouldFillFirstCol = 0 in list(zip(*matrix))[0]

    # Store the information in the 1st row/col
    for i in range(1, m):
      for j in range(1, n):
        if matrix[i][j] == 0:
          matrix[i][0] = 0
          matrix[0][j] = 0

    # Fill 0s for the matrix except the 1st row/col
    for i in range(1, m):
      for j in range(1, n):
        if matrix[i][0] == 0 or matrix[0][j] == 0:
          matrix[i][j] = 0

    # Fill 0s for the 1st row if needed
    if shouldFillFirstRow:
      matrix[0] = [0] * n

    # Fill 0s for the 1st col if needed
    if shouldFillFirstCol:
      for row in matrix:
        row[0] = 0
```


```
new Solution().setZeroes()
```


---
**Score: 5**