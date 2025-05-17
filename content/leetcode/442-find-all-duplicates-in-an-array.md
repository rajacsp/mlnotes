---
title: 442-Find-All-Duplicates-In-An-Array
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/find-all-duplicates-in-an-array


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
  def findDuplicates(self, nums: List[int]) -> List[int]:
    ans = []

    for num in nums:
      nums[abs(num) - 1] *= -1
      if nums[abs(num) - 1] > 0:
        ans.append(abs(num))

    return ans
```


```
new Solution().findDuplicates()
```


---
**Score: 5**