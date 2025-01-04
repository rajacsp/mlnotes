---
title: 283-Move-Zeroes
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/move-zeroes


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
  def moveZeroes(self, nums: List[int]) -> None:
    j = 0
    for num in nums:
      if num != 0:
        nums[j] = num
        j += 1

    for i in range(j, len(nums)):
      nums[i] = 0
```


```
new Solution().moveZeroes()
```


---
**Score: 5**