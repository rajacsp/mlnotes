---
title: 678-Valid-Parenthesis-String
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/valid-parenthesis-string


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
  def checkValidString(self, s: str) -> bool:
    low = 0
    high = 0

    for c in s:
      if c == '(':
        low += 1
        high += 1
      elif c == ')':
        if low > 0:
          low -= 1
        high -= 1
      else:
        if low > 0:
          low -= 1
        high += 1
      if high < 0:
        return False

    return low == 0
```


```
new Solution().checkValidString()
```


---
**Score: 5**