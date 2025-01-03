---
title: 893-Groups-Of-Special-Equivalent-Strings
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/groups-of-special-equivalent-strings


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
  def numSpecialEquivGroups(self, A: List[str]) -> int:
    return len({''.join(sorted(s[::2])) + ''.join(sorted(s[1::2])) for s in A})
```


```
new Solution().numSpecialEquivGroups()
```


---
**Score: 5**