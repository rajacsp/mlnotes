---
title: 268-Missing-Number
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/missing-number


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
  def missingNumber(self, nums: List[int]) -> int:
    ans = len(nums)

    for i, num in enumerate(nums):
      ans ^= i ^ num

    return ans
```


```
new Solution().missingNumber()
```


---
**Score: 5**