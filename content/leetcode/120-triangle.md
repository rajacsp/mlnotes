---
title: 120-Triangle
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/triangle


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
  def minimumTotal(self, triangle: List[List[int]]) -> int:
    for i in reversed(range(len(triangle) - 1)):
      for j in range(i + 1):
        triangle[i][j] += min(triangle[i + 1][j],
                              triangle[i + 1][j + 1])

    return triangle[0][0]
```


```
new Solution().minimumTotal()
```


---
**Score: 5**