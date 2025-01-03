---
title: 69-Sqrtx
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/sqrtx


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
  def mySqrt(self, x: int) -> int:
    l = 1
    r = x + 1

    while l < r:
      m = (l + r) // 2
      if m * m > x:
        r = m
      else:
        l = m + 1

    # L: smallest number s.t. l * l > x
    return l - 1
```


```
new Solution().mySqrt()
```


---
**Score: 5**