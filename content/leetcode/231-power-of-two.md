---
title: 231-Power-Of-Two
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/power-of-two


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
  def isPowerOfTwo(self, n: int) -> bool:
    return False if n < 0 else bin(n).count('1') == 1
```


```
new Solution().isPowerOfTwo()
```


---
**Score: 5**