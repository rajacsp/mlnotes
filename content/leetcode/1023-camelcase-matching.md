---
title: 1023-Camelcase-Matching
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/camelcase-matching


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
  def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
    def isMatch(q: str) -> bool:
      j = 0

      for i, c in enumerate(q):
        if j < len(pattern) and c == pattern[j]:
          j += 1
        elif c.isupper():
          return False

      return j == len(pattern)

    return [isMatch(q) for q in queries]
```


```
new Solution().camelMatch()
```


---
**Score: 5**