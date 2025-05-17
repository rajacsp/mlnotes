---
title: 972-Equal-Rational-Numbers
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/equal-rational-numbers


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
  def isRationalEqual(self, S: str, T: str) -> bool:
    def valueOf(s: str) -> float:
      if s.find('(') == -1:
        return float(s)

      integer_nonRepeating = float(s[:s.find('(')])
      nonRepeatingLength = s.find('(') - s.find('.') - 1
      repeating = float(s[s.find('(') + 1: s.find(')')])
      repeatingLength = s.find(')') - s.find('(') - 1

      return integer_nonRepeating + repeating * 0.1**nonRepeatingLength * ratios[repeatingLength]

    ratios = [1, 1 / 9, 1 / 99, 1 / 999, 1 / 9999]

    return abs(valueOf(S) - valueOf(T)) < 1e-9
```


```
new Solution().isRationalEqual()
```


---
**Score: 5**