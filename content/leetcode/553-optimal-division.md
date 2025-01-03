---
title: 553-Optimal-Division
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/optimal-division


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
  def optimalDivision(self, nums: List[int]) -> str:
    ans = str(nums[0])

    if len(nums) == 1:
      return ans
    if len(nums) == 2:
      return ans + '/' + str(nums[1])

    ans += '/(' + str(nums[1])
    for i in range(2, len(nums)):
      ans += '/' + str(nums[i])
    ans += ')'
    return ans
```


```
new Solution().optimalDivision()
```


---
**Score: 5**