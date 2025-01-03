---
title: 259-3Sum-Smaller
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/3sum-smaller


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
  def threeSumSmaller(self, nums: List[int], target: int) -> int:
    if len(nums) < 3:
      return 0

    ans = 0

    nums.sort()

    for i in range(len(nums) - 2):
      l = i + 1
      r = len(nums) - 1
      while l < r:
        if nums[i] + nums[l] + nums[r] < target:
          # (nums[i], nums[l], nums[r])
          # (nums[i], nums[l], nums[r - 1])
          # ...,
          # (nums[i], nums[l], nums[l + 1])
          ans += r - l
          l += 1
        else:
          r -= 1

    return ans
```


```
new Solution().threeSumSmaller()
```


---
**Score: 5**