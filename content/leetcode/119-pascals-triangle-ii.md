---
title: 119-Pascals-Triangle-Ii
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/pascals-triangle-ii


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
  def getRow(self, rowIndex: int) -> List[int]:
    ans = [1] * (rowIndex + 1)

    for i in range(2, rowIndex + 1):
      for j in range(1, i):
        ans[i - j] += ans[i - j - 1]

    return ans
```


```
new Solution().getRow()
```


---
**Score: 5**