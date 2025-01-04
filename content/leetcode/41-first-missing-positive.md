---
title: 41-First-Missing-Positive
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/first-missing-positive


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
  def firstMissingPositive(self, nums: List[int]) -> int:
    n = len(nums)

    # Correct slot:
    # nums[i] = i + 1
    # nums[i] - 1 = i
    # nums[nums[i] - 1] = nums[i]
    for i in range(n):
      while nums[i] > 0 and nums[i] <= n and nums[nums[i] - 1] != nums[i]:
        nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    for i, num in enumerate(nums):
      if num != i + 1:
        return i + 1

    return n + 1
```


```
new Solution().firstMissingPositive()
```


---
**Score: 5**