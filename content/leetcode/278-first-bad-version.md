---
title: 278-First-Bad-Version
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/first-bad-version


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
  def firstBadVersion(self, n: int) -> int:
    l = 1
    r = n

    while l < r:
      m = (l + r) >> 1
      if isBadVersion(m):
        r = m
      else:
        l = m + 1

    return l
```


```
new Solution().firstBadVersion()
```


---
**Score: 5**