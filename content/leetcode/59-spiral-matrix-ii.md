---
title: 59-Spiral-Matrix-Ii
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/spiral-matrix-ii


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
  def generateMatrix(self, n: int) -> List[List[int]]:
    ans = [[0] * n for _ in range(n)]
    count = 1

    for min in range(n // 2):
      max = n - min - 1
      for i in range(min, max):
        ans[min][i] = count
        count += 1
      for i in range(min, max):
        ans[i][max] = count
        count += 1
      for i in range(max, min, -1):
        ans[max][i] = count
        count += 1
      for i in range(max, min, -1):
        ans[i][min] = count
        count += 1

    if n & 1:
      ans[n // 2][n // 2] = count

    return ans
```


```
new Solution().generateMatrix()
```


---
**Score: 5**