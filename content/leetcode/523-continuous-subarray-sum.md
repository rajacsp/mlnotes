---
title: 523-Continuous-Subarray-Sum
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/continuous-subarray-sum


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
  def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    prefix = 0
    prefixToIndex = {0: -1}

    for i, num in enumerate(nums):
      prefix += num
      if k != 0:
        prefix %= k
      if prefix in prefixToIndex:
        if i - prefixToIndex[prefix] > 1:
          return True
      else:
        prefixToIndex[prefix] = i

    return False
```


```
new Solution().checkSubarraySum()
```


---
**Score: 5**