---
title: 172-Factorial-Trailing-Zeroes
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/factorial-trailing-zeroes


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
  def trailingZeroes(self, n: int) -> int:
    return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)
```


```
new Solution().trailingZeroes()
```


---
**Score: 5**