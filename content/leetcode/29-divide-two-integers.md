---
title: 29-Divide-Two-Integers
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/divide-two-integers


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
  def divide(self, dividend: int, divisor: int) -> int:
    if dividend == -2**31 and divisor == -1:
      return 2**31 - 1

    sign = -1 if (dividend > 0) ^ (divisor > 0) else 1
    ans = 0
    dvd = abs(dividend)
    dvs = abs(divisor)

    while dvd >= dvs:
      k = 1
      while k * 2 * dvs <= dvd:
        k <<= 1
      dvd -= k * dvs
      ans += k

    return sign * ans
```


```
new Solution().divide()
```


---
**Score: 5**