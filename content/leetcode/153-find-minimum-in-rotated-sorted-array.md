---
title: 153-Find-Minimum-In-Rotated-Sorted-Array
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array


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
  def findMin(self, nums: List[int]) -> int:
    l = 0
    r = len(nums) - 1

    while l < r:
      m = (l + r) // 2
      if nums[m] < nums[r]:
        r = m
      else:
        l = m + 1

    return nums[l]
```


```
new Solution().findMin()
```


---
**Score: 5**