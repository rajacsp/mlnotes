---
title: 1074-Number-Of-Submatrices-That-Sum-To-Target
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/number-of-submatrices-that-sum-to-target


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
  def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
    m = len(matrix)
    n = len(matrix[0])
    ans = 0

    # Transfer each row of matrix to prefix sum
    for row in matrix:
      for i in range(1, n):
        row[i] += row[i - 1]

    for baseCol in range(n):
      for j in range(baseCol, n):
        prefixCount = Counter({0: 1})
        summ = 0
        for i in range(m):
          if baseCol > 0:
            summ -= matrix[i][baseCol - 1]
          summ += matrix[i][j]
          ans += prefixCount[summ - target]
          prefixCount[summ] += 1

    return ans
```


```
new Solution().numSubmatrixSumTarget()
```


---
**Score: 5**