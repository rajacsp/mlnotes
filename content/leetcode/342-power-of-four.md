---
title: 342-Power-Of-Four
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/power-of-four


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
  def isPowerOfFour(self, n: int) -> bool:
    # Why (4^n - 1) % 3 == 0?
    # (4^n - 1) = (2^n - 1)(2^n + 1) and 2^n - 1, 2^n, 2^n + 1 are
    # Three consecutive numbers among one of them, there must be a multiple
    # Of 3, and that can't be 2^n, so it must be either 2^n - 1 or 2^n + 1.
    # Therefore, 4^n - 1 is a multiple of 3.
    return n > 0 and bin(n).count('1') == 1 and (n - 1) % 3 == 0
```


```
new Solution().isPowerOfFour()
```


---
**Score: 5**