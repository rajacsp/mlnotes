---
title: 75-Sort-Colors
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/sort-colors


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
  def sortColors(self, nums: List[int]) -> None:
    zero = -1
    one = -1
    two = -1

    for num in nums:
      if num == 0:
        two += 1
        one += 1
        zero += 1
        nums[two] = 2
        nums[one] = 1
        nums[zero] = 0
      elif num == 1:
        two += 1
        one += 1
        nums[two] = 2
        nums[one] = 1
      else:
        two += 1
        nums[two] = 2
```


```
new Solution().sortColors()
```


---
**Score: 5**