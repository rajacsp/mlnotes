---
title: 833-Find-And-Replace-In-String
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/find-and-replace-in-string


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
  def findReplaceString(self, s: str, indexes: List[int],
                        sources: List[str], targets: List[str]) -> str:
    for index, source, target in sorted(zip(indexes, sources, targets), reverse=True):
      if s[index:index + len(source)] == source:
        s = s[:index] + target + s[index + len(source):]
    return s
```


```
new Solution().findReplaceString()
```


---
**Score: 5**