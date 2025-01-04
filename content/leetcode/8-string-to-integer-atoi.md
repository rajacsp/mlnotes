---
title: 8-String-To-Integer-Atoi
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/string-to-integer-atoi


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
  def myAtoi(self, s: str) -> int:
    s = s.strip()
    if not s:
      return 0

    sign = -1 if s[0] == '-' else 1
    if s[0] in {'-', '+'}:
      s = s[1:]

    num = 0

    for c in s:
      if not c.isdigit():
        break
      num = num * 10 + ord(c) - ord('0')
      if sign * num <= -2**31:
        return -2**31
      if sign * num >= 2**31 - 1:
        return 2**31 - 1

    return sign * num
```


```
new Solution().myAtoi()
```


---
**Score: 5**