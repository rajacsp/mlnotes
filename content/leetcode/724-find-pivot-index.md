---
title: 724-Find-Pivot-Index
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/find-pivot-index


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
  def pivotIndex(self, nums: List[int]) -> int:
    summ = sum(nums)
    prefix = 0

    for i, num in enumerate(nums):
      if prefix == summ - prefix - num:
        return i
      prefix += num

    return -1
```


```
new Solution().pivotIndex()
```


---
**Score: 5**