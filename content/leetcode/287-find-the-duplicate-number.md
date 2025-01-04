---
title: 287-Find-The-Duplicate-Number
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/find-the-duplicate-number


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
  def findDuplicate(self, nums: List[int]) -> int:
    slow = nums[nums[0]]
    fast = nums[nums[nums[0]]]

    while slow != fast:
      slow = nums[slow]
      fast = nums[nums[fast]]

    slow = nums[0]

    while slow != fast:
      slow = nums[slow]
      fast = nums[fast]

    return slow
```


```
new Solution().findDuplicate()
```


---
**Score: 5**