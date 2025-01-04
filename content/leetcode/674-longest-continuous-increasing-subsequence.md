---
title: 674-Longest-Continuous-Increasing-Subsequence
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/longest-continuous-increasing-subsequence


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
  def findLengthOfLCIS(self, nums: List[int]) -> int:
    ans = 0
    j = 0

    for i in range(len(nums)):
      if i > 0 and nums[i] <= nums[i - 1]:
        j = i
      ans = max(ans, i - j + 1)

    return ans
```


```
new Solution().findLengthOfLCIS()
```


---
**Score: 5**