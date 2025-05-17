---
title: 686-Repeated-String-Match
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/repeated-string-match


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
  def repeatedStringMatch(self, a: str, b: str) -> int:
    n = ceil(len(b) / len(a))
    s = a * n
    if b in s:
      return n
    if b in s + a:
      return n + 1
    return -1
```


```
new Solution().repeatedStringMatch()
```


---
**Score: 5**