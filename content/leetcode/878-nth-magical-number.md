---
title: 878-Nth-Magical-Number
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/nth-magical-number


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
  def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
    lcm = a * b // math.gcd(a, b)
    l = min(a, b)
    r = min(a, b) * n

    while l < r:
      m = (l + r) // 2
      if m // a + m // b - m // lcm >= n:
        r = m
      else:
        l = m + 1

    return l % (10**9 + 7)
```


```
new Solution().nthMagicalNumber()
```


---
**Score: 5**