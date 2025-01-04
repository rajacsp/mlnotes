---
title: 644-Maximum-Average-Subarray-Ii
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/maximum-average-subarray-ii


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
  def findMaxAverage(self, nums: List[int], k: int) -> float:
    kErr = 1e-5
    l = min(nums)
    r = max(nums)

    # True if there's a subarray with length >= k and average sum >= m
    def check(m: float) -> bool:
      summ = 0
      prevSum = 0
      minPrevSum = 0

      for i, num in enumerate(nums):
        # Trick: -m for each num so that we can check if the sum of the
        # Subarray >= 0
        summ += num - m
        if i >= k:
          prevSum += nums[i - k] - m
          minPrevSum = min(minPrevSum, prevSum)
        # If sum - minPrevSum >= 0,
        # We know there's a subarray with length >= k and average sum >= m
        if i + 1 >= k and summ >= minPrevSum:
          return True

      return False

    while r - l > kErr:
      m = (l + r) / 2
      if check(m):
        l = m
      else:
        r = m

    return l
```


```
new Solution().findMaxAverage()
```


---
**Score: 5**