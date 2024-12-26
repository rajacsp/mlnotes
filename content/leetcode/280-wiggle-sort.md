---
title: 280-Wiggle-Sort
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/wiggle-sort


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
  def wiggleSort(self, nums: List[int]) -> None:
    # 1. if i is even, then nums[i] <= nums[i - 1]
    # 2. if i is odd, then nums[i] >= nums[i - 1]
    for i in range(1, len(nums)):
      if not (i & 1) and nums[i] > nums[i - 1] or \
              (i & 1) and nums[i] < nums[i - 1]:
        nums[i], nums[i - 1] = nums[i - 1], nums[i]
```


```
new Solution().wiggleSort()
```


---
**Score: 5**