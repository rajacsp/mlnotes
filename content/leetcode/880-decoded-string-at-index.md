---
title: 880-Decoded-String-At-Index
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/decoded-string-at-index


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
  def decodeAtIndex(self, s: str, k: int) -> str:
    size = 0

    for c in s:
      if c.isdigit():
        size *= int(c)
      else:
        size += 1

    for c in reversed(s):
      k %= size
      if k == 0 and c.isalpha():
        return c
      if c.isdigit():
        size //= int(c)
      else:
        size -= 1
```


```
new Solution().decodeAtIndex()
```


---
**Score: 5**