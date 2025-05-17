---
title: 263-Ugly-Number
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/ugly-number


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
  def isUgly(self, n: int) -> bool:
    if n == 0:
      return False

    for prime in 2, 3, 5:
      while n % prime == 0:
        n //= prime

    return n == 1
```


```
new Solution().isUgly()
```


---
**Score: 5**