---
title: 7-Reverse-Integer
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/reverse-integer


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
  def reverse(self, x: int) -> int:
    ans = 0
    sign = -1 if x < 0 else 1
    x *= sign

    while x:
      ans = ans * 10 + x % 10
      x //= 10

    return 0 if ans < -2**31 or ans > 2**31 - 1 else sign * ans
```


```
new Solution().reverse()
```


---
**Score: 5**