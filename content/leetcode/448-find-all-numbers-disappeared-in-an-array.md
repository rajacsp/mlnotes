---
title: 448-Find-All-Numbers-Disappeared-In-An-Array
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array


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
  def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    for num in nums:
      index = abs(num) - 1
      nums[index] = -abs(nums[index])

    return [i + 1 for i, num in enumerate(nums) if num > 0]
```


```
new Solution().findDisappearedNumbers()
```


---
**Score: 5**