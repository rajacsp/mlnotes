---
title: 118-Pascals-Triangle
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/pascals-triangle


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
  def generate(self, numRows: int) -> List[List[int]]:
    ans = []

    for i in range(numRows):
      ans.append([1] * (i + 1))

    for i in range(2, numRows):
      for j in range(1, len(ans[i]) - 1):
        ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]

    return ans
```


```
new Solution().generate()
```


---
**Score: 5**