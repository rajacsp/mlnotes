---
title: 1089-Duplicate-Zeros
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/duplicate-zeros


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
  def duplicateZeros(self, arr: List[int]) -> None:
    zeros = arr.count(0)
    i = len(arr) - 1
    j = len(arr) + zeros - 1

    while i < j:
      if j < len(arr):
        arr[j] = arr[i]
      if arr[i] == 0:
        j -= 1
        if j < len(arr):
          arr[j] = arr[i]
      i -= 1
      j -= 1
```


```
new Solution().duplicateZeros()
```


---
**Score: 5**