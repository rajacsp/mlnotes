---
title: 162-Find-Peak-Element
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/find-peak-element


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
  def findPeakElement(self, nums: List[int]) -> int:
    l = 0
    r = len(nums) - 1

    while l < r:
      m = (l + r) // 2
      if nums[m] >= nums[m + 1]:
        r = m
      else:
        l = m + 1

    return l
```


```
new Solution().findPeakElement()
```


---
**Score: 5**