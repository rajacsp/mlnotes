---
title: 396-Rotate-Function
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/rotate-function


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
  def maxRotateFunction(self, nums: List[int]) -> int:
    f = sum(i * num for i, num in enumerate(nums))
    ans = f
    summ = sum(nums)

    for a in reversed(nums):
      f += summ - len(nums) * a
      ans = max(ans, f)

    return ans
```


```
new Solution().maxRotateFunction()
```


---
**Score: 5**