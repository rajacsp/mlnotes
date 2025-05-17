---
title: 628-Maximum-Product-Of-Three-Numbers
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/maximum-product-of-three-numbers


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
  def maximumProduct(self, nums: List[int]) -> int:
    nums.sort()
    return max(nums[-1] * nums[0] * nums[1],
               nums[-1] * nums[-2] * nums[-3])
```


```
new Solution().maximumProduct()
```


---
**Score: 5**