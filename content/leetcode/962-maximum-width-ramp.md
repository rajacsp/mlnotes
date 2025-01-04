---
title: 962-Maximum-Width-Ramp
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/maximum-width-ramp


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
  def maxWidthRamp(self, nums: List[int]) -> int:
    ans = 0
    stack = []

    for i, num in enumerate(nums):
      if stack == [] or num <= nums[stack[-1]]:
        stack.append(i)

    for i, num in reversed(list(enumerate(nums))):
      while stack and num >= nums[stack[-1]]:
        ans = max(ans, i - stack.pop())

    return ans
```


```
new Solution().maxWidthRamp()
```


---
**Score: 5**