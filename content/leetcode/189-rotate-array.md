---
title: 189-Rotate-Array
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/rotate-array


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
  def rotate(self, nums: List[int], k: int) -> None:
    k %= len(nums)
    self.reverse(nums, 0, len(nums) - 1)
    self.reverse(nums, 0, k - 1)
    self.reverse(nums, k, len(nums) - 1)

  def reverse(self, nums: List[int], l: int, r: int) -> None:
    while l < r:
      nums[l], nums[r] = nums[r], nums[l]
      l += 1
      r -= 1
```


```
new Solution().rotate()
```


---
**Score: 5**