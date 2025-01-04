---
title: 34-Find-First-And-Last-Position-Of-Element-In-Sorted-Array
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array


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
  def searchRange(self, nums: List[int], target: int) -> List[int]:
    l = bisect_left(nums, target)
    if l == len(nums) or nums[l] != target:
      return -1, -1
    r = bisect_right(nums, target) - 1
    return l, r
```


```
new Solution().searchRange()
```


---
**Score: 5**