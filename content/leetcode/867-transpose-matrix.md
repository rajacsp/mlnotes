---
title: 867-Transpose-Matrix
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/transpose-matrix


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
  def transpose(self, A: List[List[int]]) -> List[List[int]]:
    ans = [[0] * len(A) for _ in range(len(A[0]))]

    for i in range(len(A)):
      for j in range(len(A[0])):
        ans[j][i] = A[i][j]

    return ans
```


```
new Solution().transpose()
```


---
**Score: 5**