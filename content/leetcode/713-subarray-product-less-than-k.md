---
title: 713-Subarray-Product-Less-Than-K
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/subarray-product-less-than-k


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
  def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    if k <= 1:
      return 0

    ans = 0
    prod = 1

    j = 0
    for i, num in enumerate(nums):
      prod *= num
      while prod >= k:
        prod /= nums[j]
        j += 1
      ans += i - j + 1

    return ans
```


```
new Solution().numSubarrayProductLessThanK()
```


---
**Score: 5**