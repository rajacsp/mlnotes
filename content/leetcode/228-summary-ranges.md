---
title: 228-Summary-Ranges
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/summary-ranges


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
  def summaryRanges(self, nums: List[int]) -> List[str]:
    ans = []

    i = 0
    while i < len(nums):
      begin = nums[i]
      while i < len(nums) - 1 and nums[i] == nums[i + 1] - 1:
        i += 1
      end = nums[i]
      if begin == end:
        ans.append(str(begin))
      else:
        ans.append(str(begin) + "->" + str(end))
      i += 1

    return ans
```


```
new Solution().summaryRanges()
```


---
**Score: 5**