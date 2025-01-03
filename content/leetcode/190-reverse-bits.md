---
title: 190-Reverse-Bits
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/reverse-bits


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
  def reverseBits(self, n: int) -> int:
    ans = 0

    for i in range(32):
      if n >> i & 1:
        ans |= 1 << 31 - i

    return ans
```


```
new Solution().reverseBits()
```


---
**Score: 5**