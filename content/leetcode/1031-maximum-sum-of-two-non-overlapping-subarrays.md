---
title: 1031-Maximum-Sum-Of-Two-Non-Overlapping-Subarrays
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays


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
  def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
    def helper(l: int, r: int) -> int:
      n = len(nums)
      left = [0] * n
      summ = 0

      for i in range(n):
        summ += nums[i]
        if i >= l:
          summ -= nums[i - l]
        if i >= l - 1:
          left[i] = max(left[i - 1], summ) if i > 0 else summ

      right = [0] * n
      summ = 0

      for i in reversed(range(n)):
        summ += nums[i]
        if i <= n - r - 1:
          summ -= nums[i + r]
        if i <= n - r:
          right[i] = max(right[i + 1], summ) if i < n - 1 else summ

      return max(left[i] + right[i + 1] for i in range(n - 1))

    return max(helper(firstLen, secondLen), helper(secondLen, firstLen))
```


```
new Solution().maxSumTwoNoOverlap()
```


---
**Score: 5**