---
title: 367-Valid-Perfect-Square
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/valid-perfect-square


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
  def isPerfectSquare(self, num: int) -> bool:
    l = 1
    r = num

    while l < r:
      m = (l + r) // 2
      if m >= num / m:
        r = m
      else:
        l = m + 1

    return l * l == num
```


```
new Solution().isPerfectSquare()
```


---
**Score: 5**