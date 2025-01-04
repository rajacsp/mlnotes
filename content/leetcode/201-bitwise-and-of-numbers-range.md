---
title: 201-Bitwise-And-Of-Numbers-Range
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/bitwise-and-of-numbers-range


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
  def rangeBitwiseAnd(self, m: int, n: int) -> int:
    return self.rangeBitwiseAnd(m >> 1, n >> 1) << 1 if m < n else m
```


```
new Solution().rangeBitwiseAnd()
```


---
**Score: 5**