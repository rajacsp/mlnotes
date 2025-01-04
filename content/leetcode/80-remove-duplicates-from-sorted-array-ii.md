---
title: 80-Remove-Duplicates-From-Sorted-Array-Ii
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii


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
  def removeDuplicates(self, nums: List[int]) -> int:
    i = 0

    for num in nums:
      if i < 2 or num != nums[i - 2]:
        nums[i] = num
        i += 1

    return i
```


```
new Solution().removeDuplicates()
```


---
**Score: 5**