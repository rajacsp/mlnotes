---
title: 581-Shortest-Unsorted-Continuous-Subarray
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/shortest-unsorted-continuous-subarray


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
  def findUnsortedSubarray(self, nums: List[int]) -> int:
    mini = math.inf
    maxi = -math.inf
    flag = False

    for i in range(1, len(nums)):
      if nums[i] < nums[i - 1]:
        flag = True
      if flag:
        mini = min(mini, nums[i])

    flag = False

    for i in reversed(range(len(nums) - 1)):
      if nums[i] > nums[i + 1]:
        flag = True
      if flag:
        maxi = max(maxi, nums[i])

    for l in range(len(nums)):
      if nums[l] > mini:
        break

    for r, num in reversed(list(enumerate(nums))):
      if num < maxi:
        break

    return 0 if l >= r else r - l + 1
```


```
new Solution().findUnsortedSubarray()
```


---
**Score: 5**