---
title: 48-Rotate-Image
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/rotate-image


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
  def rotate(self, matrix: List[List[int]]) -> None:
    matrix.reverse()

    for i in range(len(matrix)):
      for j in range(i + 1, len(matrix)):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```


```
new Solution().rotate()
```


---
**Score: 5**