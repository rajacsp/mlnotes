---
title: 890-Find-And-Replace-Pattern
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/find-and-replace-pattern


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
  def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
    def isIsomorphic(w: str, p: str) -> bool:
      return [*map(w.index, w)] == [*map(p.index, p)]
    return [word for word in words if isIsomorphic(word, pattern)]
```


```
new Solution().findAndReplacePattern()
```


---
**Score: 5**