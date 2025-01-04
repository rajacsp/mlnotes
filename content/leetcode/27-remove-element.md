---
title: 27-Remove-Element
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/remove-element


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
  def removeElement(self, nums: List[int], val: int) -> int:
    i = 0

    for num in nums:
      if num != val:
        nums[i] = num
        i += 1

    return i
```


```
new Solution().removeElement()
```


---
**Score: 5**