---
title: 81-Search-In-Rotated-Sorted-Array-Ii
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/search-in-rotated-sorted-array-ii


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
  def search(self, nums: List[int], target: int) -> bool:
    l = 0
    r = len(nums) - 1

    while l <= r:
      m = (l + r) // 2
      if nums[m] == target:
        return True
      if nums[l] == nums[m] == nums[r]:
        l += 1
        r -= 1
      elif nums[l] <= nums[m]:  # nums[l..m] are sorted
        if nums[l] <= target < nums[m]:
          r = m - 1
        else:
          l = m + 1
      else:  # nums[m..n - 1] are sorted
        if nums[m] < target <= nums[r]:
          l = m + 1
        else:
          r = m - 1

    return False
```


```
new Solution().search()
```


---
**Score: 5**