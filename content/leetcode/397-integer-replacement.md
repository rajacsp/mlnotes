---
title: 397-Integer-Replacement
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/integer-replacement


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
  def integerReplacement(self, n: int) -> int:
    ans = 0

    while n > 1:
      if (n & 1) == 0:
        n >>= 1
      elif n == 3 or ((n >> 1) & 1) == 0:
        n -= 1
      else:
        n += 1
      ans += 1

    return ans
```


```
new Solution().integerReplacement()
```


---
**Score: 5**