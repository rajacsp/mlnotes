---
title: 371-Sum-Of-Two-Integers
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/sum-of-two-integers


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
  def getSum(self, a: int, b: int) -> int:
    mask = 0xFFFFFFFF
    kMax = 2000

    while b:
      a, b = (a ^ b) & mask, ((a & b) << 1) & mask

    return a if a < kMax else ~(a ^ mask)
```


```
new Solution().getSum()
```


---
**Score: 5**