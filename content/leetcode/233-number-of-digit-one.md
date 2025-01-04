---
title: 233-Number-Of-Digit-One
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/number-of-digit-one


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
  def countDigitOne(self, n: int) -> int:
    ans = 0

    pow10 = 1
    while pow10 <= n:
      divisor = pow10 * 10
      quotient = n // divisor
      remainder = n % divisor
      if quotient > 0:
        ans += quotient * pow10
      if remainder >= pow10:
        ans += min(remainder - pow10 + 1, pow10)
      pow10 *= 10

    return ans
```


```
new Solution().countDigitOne()
```


---
**Score: 5**