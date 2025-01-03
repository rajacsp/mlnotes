---
title: 275-H-Index-Ii
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/h-index-ii


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
  def hIndex(self, citations: List[int]) -> int:
    l = 0
    r = len(citations)

    while l < r:
      m = (l + r) // 2
      if citations[m] >= len(citations) - m:
        r = m
      else:
        l = m + 1

    return len(citations) - l
```


```
new Solution().hIndex()
```


---
**Score: 5**