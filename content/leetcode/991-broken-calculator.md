---
title: 991-Broken-Calculator
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/broken-calculator


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
  def brokenCalc(self, X: int, Y: int) -> int:
    ops = 0

    while X < Y:
      if Y % 2 == 0:
        Y //= 2
      else:
        Y += 1
      ops += 1

    return ops + X - Y
```


```
new Solution().brokenCalc()
```


---
**Score: 5**