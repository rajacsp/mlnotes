---
title: 344-Reverse-String
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/reverse-string


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
  def reverseString(self, s: List[str]) -> None:
    l = 0
    r = len(s) - 1

    while l < r:
      s[l], s[r] = s[r], s[l]
      l += 1
      r -= 1
```


```
new Solution().reverseString()
```


---
**Score: 5**