---
title: 152-Maximum-Product-Subarray
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/maximum-product-subarray


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
  def maxProduct(self, nums: List[int]) -> int:
    ans = nums[0]
    prevMin = nums[0]
    prevMax = nums[0]

    for i in range(1, len(nums)):
      mini = prevMin * nums[i]
      maxi = prevMax * nums[i]
      prevMin = min(nums[i], mini, maxi)
      prevMax = max(nums[i], mini, maxi)
      ans = max(ans, prevMax)

    return ans
```


```
new Solution().maxProduct()
```


---
**Score: 5**