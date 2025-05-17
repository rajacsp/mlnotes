---
title: 788-Rotated-Digits
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/rotated-digits


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
  def rotatedDigits(self, N: int) -> int:
    def isGoodNumber(i: int) -> bool:
      isRotated = False

      for c in str(i):
        if c == '0' or c == '1' or c == '8':
          continue
        if c == '2' or c == '5' or c == '6' or c == '9':
          isRotated = True
        else:
          return False

      return isRotated

    return sum(isGoodNumber(i) for i in range(1, N + 1))
```


```
new Solution().rotatedDigits()
```


---
**Score: 5**