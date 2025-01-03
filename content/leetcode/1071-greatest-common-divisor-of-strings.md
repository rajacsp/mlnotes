---
title: 1071-Greatest-Common-Divisor-Of-Strings
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/greatest-common-divisor-of-strings


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
  def gcdOfStrings(self, str1: str, str2: str) -> str:
    def mod(s1: str, s2: str) -> str:
      while s1.startswith(s2):
        s1 = s1[len(s2):]
      return s1

    if len(str1) < len(str2):
      return self.gcdOfStrings(str2, str1)
    if not str1.startswith(str2):
      return ''
    if not str2:
      return str1
    return self.gcdOfStrings(str2, mod(str1, str2))
```


```
new Solution().gcdOfStrings()
```


---
**Score: 5**