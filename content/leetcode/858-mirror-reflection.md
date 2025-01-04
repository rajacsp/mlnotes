---
title: 858-Mirror-Reflection
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/mirror-reflection


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
  def mirrorReflection(self, p: int, q: int) -> int:
    while p % 2 == 0 and q % 2 == 0:
      p //= 2
      q //= 2

    if p % 2 == 0:
      return 2
    if q % 2 == 0:
      return 0
    return 1
```


```
new Solution().mirrorReflection()
```


---
**Score: 5**