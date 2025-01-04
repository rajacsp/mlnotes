---
title: 290-Word-Pattern
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/word-pattern


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
  def wordPattern(self, pattern: str, str: str) -> bool:
    t = str.split()
    return [*map(pattern.index, pattern)] == [*map(t.index, t)]
```


```
new Solution().wordPattern()
```


---
**Score: 5**