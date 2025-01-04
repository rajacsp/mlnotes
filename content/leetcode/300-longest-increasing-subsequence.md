---
title: 300-Longest-Increasing-Subsequence
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/longest-increasing-subsequence


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
  def lengthOfLIS(self, nums: List[int]) -> int:
    if not nums:
      return 0

    # dp[i] := LIS ending at nums[i]
    dp = [1] * len(nums)

    for i in range(1, len(nums)):
      for j in range(i):
        if nums[j] < nums[i]:
          dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
```


```
new Solution().lengthOfLIS()
```


---
**Score: 5**