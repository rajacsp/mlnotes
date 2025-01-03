---
title: 921-Minimum-Add-To-Make-Parentheses-Valid
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/minimum-add-to-make-parentheses-valid


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
  def minAddToMakeValid(self, s: str) -> int:
    l = 0
    r = 0

    for c in s:
      if c == '(':
        l += 1
      else:
        if l == 0:
          r += 1
        else:
          l -= 1

    return l + r
```


```
new Solution().minAddToMakeValid()
```


---
**Score: 5**