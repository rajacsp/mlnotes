---
title: 1003-Check-If-Word-Is-Valid-After-Substitutions
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/check-if-word-is-valid-after-substitutions


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
  def isValid(self, s: str) -> bool:
    stack = []

    for c in s:
      if c == 'c':
        if len(stack) < 2 or stack[-2] != 'a' or stack[-1] != 'b':
          return False
        stack.pop()
        stack.pop()
      else:
        stack.append(c)

    return not stack
```


```
new Solution().isValid()
```


---
**Score: 5**