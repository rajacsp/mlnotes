---
title: 50-Powx-N
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/powx-n


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
  def myPow(self, x: float, n: int) -> float:
    if n == 0:
      return 1
    if n < 0:
      return 1 / self.myPow(x, -n)
    if n & 1:
      return x * self.myPow(x, n - 1)
    return self.myPow(x * x, n // 2)
```


```
new Solution().myPow()
```


---
**Score: 5**