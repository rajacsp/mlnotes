---
title: 1009-Complement-Of-Base-10-Integer
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/complement-of-base-10-integer


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
  def bitwiseComplement(self, N: int) -> int:
    mask = 1

    while mask < N:
      mask = (mask << 1) + 1

    return mask ^ N
```


```
new Solution().bitwiseComplement()
```


---
**Score: 5**