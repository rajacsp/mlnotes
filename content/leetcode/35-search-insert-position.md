---
title: 35-Search-Insert-Position
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/search-insert-position


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
  def searchInsert(self, nums: List[int], target: int) -> int:
    l = 0
    r = len(nums)

    while l < r:
      m = (l + r) // 2
      if nums[m] == target:
        return m
      if nums[m] < target:
        l = m + 1
      else:
        r = m

    return l
```


```
new Solution().searchInsert()
```


---
**Score: 5**