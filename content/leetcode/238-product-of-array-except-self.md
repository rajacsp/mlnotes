---
title: 238-Product-Of-Array-Except-Self
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/product-of-array-except-self


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
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    prefix = [1] * n  # Prefix product
    suffix = [1] * n  # Suffix product

    for i in range(1, n):
      prefix[i] = prefix[i - 1] * nums[i - 1]

    for i in reversed(range(n - 1)):
      suffix[i] = suffix[i + 1] * nums[i + 1]

    return [prefix[i] * suffix[i] for i in range(n)]
```


```
new Solution().productExceptSelf()
```


---
**Score: 5**