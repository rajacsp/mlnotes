---
title: 161-One-Edit-Distance
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/one-edit-distance


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
  def isOneEditDistance(self, s: str, t: str) -> bool:
    m = len(s)
    n = len(t)
    if m > n:  # Make sure len(s) <= len(t)
      return self.isOneEditDistance(t, s)

    for i in range(m):
      if s[i] != t[i]:
        if m == n:
          return s[i + 1:] == t[i + 1:]  # Replace s[i] with t[i]
        return s[i:] == t[i + 1:]  # Delete t[i]

    return m + 1 == n  # Delete t[-1]
```


```
new Solution().isOneEditDistance()
```


---
**Score: 5**