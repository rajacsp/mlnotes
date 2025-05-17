---
title: 258-Add-Digits
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/add-digits


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
  def addDigits(self, num: int) -> int:
    return 0 if num == 0 else 1 + (num - 1) % 9
```


```
new Solution().addDigits()
```


---
**Score: 5**