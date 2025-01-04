---
title: 71-Simplify-Path
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/simplify-path


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
  def simplifyPath(self, path: str) -> str:
    stack = []

    for str in path.split('/'):
      if str in ('', '.'):
        continue
      if str == '..':
        if stack:
          stack.pop()
      else:
        stack.append(str)

    return '/' + '/'.join(stack)
```


```
new Solution().simplifyPath()
```


---
**Score: 5**