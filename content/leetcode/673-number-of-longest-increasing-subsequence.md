---
title: 673-Number-Of-Longest-Increasing-Subsequence
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/number-of-longest-increasing-subsequence


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
  def findNumberOfLIS(self, nums: List[int]) -> int:
    ans = 0
    maxLength = 0
    length = [1] * len(nums)  # length[i] := LIS's length ending w/ nums[i]
    count = [1] * len(nums)  # count[i] := # Of the LIS ending w/ nums[i]

    # Calculate length and count arrays
    for i, num in enumerate(nums):
      for j in range(i):
        if nums[j] < num:
          if length[i] < length[j] + 1:
            length[i] = length[j] + 1
            count[i] = count[j]
          elif length[i] == length[j] + 1:
            count[i] += count[j]

    # Get # Of LIS
    for i, l in enumerate(length):
      if l > maxLength:
        maxLength = l
        ans = count[i]
      elif l == maxLength:
        ans += count[i]

    return ans
```


```
new Solution().findNumberOfLIS()
```


---
**Score: 5**