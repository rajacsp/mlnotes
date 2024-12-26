---
title: 537-Complex-Number-Multiplication
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/complex-number-multiplication


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
  def complexNumberMultiply(self, a: str, b: str) -> str:
    def getRealAndImag(s: str) -> tuple:
      return int(s[:s.index('+')]), int(s[s.index('+') + 1:-1])

    A, B = getRealAndImag(a)
    C, D = getRealAndImag(b)

    return str(A * C - B * D) + '+' + str(A * D + B * C) + 'i'
```


```
new Solution().complexNumberMultiply()
```


---
**Score: 5**