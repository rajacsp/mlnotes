---
title: 661-Image-Smoother
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/image-smoother


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
  def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
    m = len(M)
    n = len(M[0])
    ans = [[0 for j in range(n)] for i in range(m)]

    for i in range(m):
      for j in range(n):
        ones = 0
        count = 0
        for y in range(max(0, i - 1), min(m, i + 2)):
          for x in range(max(0, j - 1), min(n, j + 2)):
            ones += M[y][x]
            count += 1
        ans[i][j] = ones // count

    return ans
```


```
new Solution().imageSmoother()
```


---
**Score: 5**