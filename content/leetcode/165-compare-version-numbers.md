---
title: 165-Compare-Version-Numbers
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/compare-version-numbers


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
  def compareVersion(self, version1: str, version2: str) -> int:
    levels1 = version1.split('.')
    levels2 = version2.split('.')
    length = max(len(levels1), len(levels2))

    for i in range(length):
      v1 = int(levels1[i]) if i < len(levels1) else 0
      v2 = int(levels2[i]) if i < len(levels2) else 0
      if v1 < v2:
        return -1
      if v1 > v2:
        return 1

    return 0
```


```
new Solution().compareVersion()
```


---
**Score: 5**