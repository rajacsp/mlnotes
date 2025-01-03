---
title: 487-Max-Consecutive-Ones-Ii
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/max-consecutive-ones-ii


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
  def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    ans = 0
    zeros = 0

    l = 0
    for r, num in enumerate(nums):
      if num == 0:
        zeros += 1
      while zeros == 2:
        if nums[l] == 0:
          zeros -= 1
        l += 1
      ans = max(ans, r - l + 1)

    return ans
```


```
new Solution().findMaxConsecutiveOnes()
```


---
**Score: 5**