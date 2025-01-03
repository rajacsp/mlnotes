---
title: 53-Maximum-Subarray
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/maximum-subarray


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
  def maxSubArray(self, nums: List[int]) -> int:
    ans = -math.inf
    summ = 0

    for num in nums:
      summ += num
      ans = max(ans, summ)
      summ = max(summ, 0)

    return ans
```


```
new Solution().maxSubArray()
```


---
**Score: 5**