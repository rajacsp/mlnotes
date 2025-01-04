---
title: 852-Peak-Index-In-A-Mountain-Array
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/peak-index-in-a-mountain-array


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
  def peakIndexInMountainArray(self, arr: List[int]) -> int:
    l = 0
    r = len(arr) - 1

    while l < r:
      m = (l + r) // 2
      if arr[m] < arr[m + 1]:
        l = m + 1
      else:
        r = m

    return l
```


```
new Solution().peakIndexInMountainArray()
```


---
**Score: 5**