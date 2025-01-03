---
title: 645-Set-Mismatch
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/set-mismatch


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
  def findErrorNums(self, nums: List[int]) -> List[int]:
    for num in nums:
      if nums[abs(num) - 1] < 0:
        duplicate = abs(num)
      else:
        nums[abs(num) - 1] *= -1

    for i, num in enumerate(nums):
      if num > 0:
        return [duplicate, i + 1]
```


```
new Solution().findErrorNums()
```


---
**Score: 5**