---
title: 343-Integer-Break
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/integer-break


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
  def integerBreak(self, n: int) -> int:
    if n == 2:
      return 1
    if n == 3:
      return 2

    ans = 1

    while n > 4:
      n -= 3
      ans *= 3
    ans *= n

    return ans
```


```
new Solution().integerBreak()
```


---
**Score: 5**