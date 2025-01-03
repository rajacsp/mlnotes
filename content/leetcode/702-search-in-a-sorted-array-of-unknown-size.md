---
title: 702-Search-In-A-Sorted-Array-Of-Unknown-Size
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size


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
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# Class ArrayReader:
#   def get(self, index: int) -> int:

class Solution:
  def search(self, reader: 'ArrayReader', target: int) -> int:
    l = 0
    r = 10**4

    while l < r:
      m = (l + r) // 2
      if reader.get(m) < target:
        l = m + 1
      else:
        r = m

    return l if reader.get(l) == target else -1
```


```
new Solution().search()
```


---
**Score: 5**