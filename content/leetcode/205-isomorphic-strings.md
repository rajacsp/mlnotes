---
title: 205-Isomorphic-Strings
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/isomorphic-strings


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
  def isIsomorphic(self, s: str, t: str) -> bool:
    return [*map(s.index, s)] == [*map(t.index, t)]
```


```
new Solution().isIsomorphic()
```


---
**Score: 5**