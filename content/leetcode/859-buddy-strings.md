---
title: 859-Buddy-Strings
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/buddy-strings


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
  def buddyStrings(self, A: str, B: str) -> bool:
    if len(A) != len(B):
      return False
    if A == B and len(set(A)) < len(A):
      return True

    diff = [(a, b) for a, b in zip(A, B) if a != b]

    return len(diff) == 2 and diff[0] == diff[1][::-1]
```


```
new Solution().buddyStrings()
```


---
**Score: 5**