---
title: 1006-Clumsy-Factorial
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/clumsy-factorial


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
  def clumsy(self, N: int) -> int:
    if N == 1:
      return 1
    if N == 2:
      return 2
    if N == 3:
      return 6
    if N == 4:
      return 7
    if N % 4 == 1:
      return N + 2
    if N % 4 == 2:
      return N + 2
    if N % 4 == 3:
      return N - 1
    return N + 1
```


```
new Solution().clumsy()
```


---
**Score: 5**