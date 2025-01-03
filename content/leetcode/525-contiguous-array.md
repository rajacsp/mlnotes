---
title: 525-Contiguous-Array
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/contiguous-array


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
  def findMaxLength(self, nums: List[int]) -> int:
    ans = 0
    prefix = 0
    prefixToIndex = {0: -1}

    for i, num in enumerate(nums):
      prefix += 1 if num else -1
      if prefix in prefixToIndex:
        ans = max(ans, i - prefixToIndex[prefix])
      else:
        prefixToIndex[prefix] = i

    return ans
```


```
new Solution().findMaxLength()
```


---
**Score: 5**