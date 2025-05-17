---
title: 540-Single-Element-In-A-Sorted-Array
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/single-element-in-a-sorted-array


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
  def singleNonDuplicate(self, nums: List[int]) -> int:
    l = 0
    r = len(nums) - 1

    while l < r:
      m = (l + r) // 2
      if m % 2 == 1:
        m -= 1
      if nums[m] == nums[m + 1]:
        l = m + 2
      else:
        r = m

    return nums[l]
```


```
new Solution().singleNonDuplicate()
```


---
**Score: 5**