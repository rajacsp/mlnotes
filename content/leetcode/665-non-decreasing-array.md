---
title: 665-Non-Decreasing-Array
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/non-decreasing-array


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
  def checkPossibility(self, nums: List[int]) -> bool:
    j = None

    for i in range(len(nums) - 1):
      if nums[i] > nums[i + 1]:
        if j is not None:
          return False
        j = i

    return j is None or j == 0 or j == len(nums) - 2 or \
        nums[j - 1] <= nums[j + 1] or nums[j] <= nums[j + 2]
```


```
new Solution().checkPossibility()
```


---
**Score: 5**