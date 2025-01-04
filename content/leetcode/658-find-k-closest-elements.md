---
title: 658-Find-K-Closest-Elements
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/find-k-closest-elements


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
  def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    l = 0
    r = len(arr) - k

    while l < r:
      m = (l + r) // 2
      if x - arr[m] <= arr[m + k] - x:
        r = m
      else:
        l = m + 1

    return arr[l:l + k]
```


```
new Solution().findClosestElements()
```


---
**Score: 5**