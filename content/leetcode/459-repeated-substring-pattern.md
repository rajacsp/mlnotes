---
title: 459-Repeated-Substring-Pattern
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/repeated-substring-pattern


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
  def repeatedSubstringPattern(self, s: str) -> bool:
    return s in (s + s)[1:-1]
```


```
new Solution().repeatedSubstringPattern()
```


---
**Score: 5**