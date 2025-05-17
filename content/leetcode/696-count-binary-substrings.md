---
title: 696-Count-Binary-Substrings
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/count-binary-substrings


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
  def countBinarySubstrings(self, s: str) -> int:
    ans = 0
    prevCount = 0
    equals = 1

    for i in range(len(s) - 1):
      if s[i] == s[i + 1]:
        equals += 1
      else:
        ans += min(prevCount, equals)
        prevCount = equals
        equals = 1

    return ans + min(prevCount, equals)
```


```
new Solution().countBinarySubstrings()
```


---
**Score: 5**