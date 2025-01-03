---
title: 76-Minimum-Window-Substring
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/minimum-window-substring


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
  def minWindow(self, s: str, t: str) -> str:
    count = Counter(t)
    required = len(t)
    bestLeft = -1
    minLength = len(s) + 1

    l = 0
    for r, c in enumerate(s):
      count[c] -= 1
      if count[c] >= 0:
        required -= 1
      while required == 0:
        if r - l + 1 < minLength:
          bestLeft = l
          minLength = r - l + 1
        count[s[l]] += 1
        if count[s[l]] > 0:
          required += 1
        l += 1

    return '' if bestLeft == -1 else s[bestLeft: bestLeft + minLength]
```


```
new Solution().minWindow()
```


---
**Score: 5**