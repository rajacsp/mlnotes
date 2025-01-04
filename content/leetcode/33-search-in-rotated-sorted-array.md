---
title: 33-Search-In-Rotated-Sorted-Array
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/search-in-rotated-sorted-array


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
  def search(self, nums: List[int], target: int) -> int:
    l = 0
    r = len(nums) - 1

    while l <= r:
      m = (l + r) // 2
      if nums[m] == target:
        return m
      if nums[l] <= nums[m]:  # nums[l..m] are sorted
        if nums[l] <= target < nums[m]:
          r = m - 1
        else:
          l = m + 1
      else:  # nums[m..n - 1] are sorted
        if nums[m] < target <= nums[r]:
          l = m + 1
        else:
          r = m - 1

    return -1
```


```
new Solution().search()
```


---
**Score: 5**