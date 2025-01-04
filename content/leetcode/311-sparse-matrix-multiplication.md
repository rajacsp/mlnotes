---
title: 311-Sparse-Matrix-Multiplication
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/sparse-matrix-multiplication


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
  def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
    m = len(mat1)
    n = len(mat2)
    l = len(mat2[0])
    ans = [[0] * l for _ in range(m)]

    for i in range(m):
      for j in range(l):
        for k in range(n):
          ans[i][j] += mat1[i][k] * mat2[k][j]

    return ans
```


```
new Solution().multiply()
```


---
**Score: 5**