---
title: 209-Minimum-Size-Subarray-Sum
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/minimum-size-subarray-sum


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
  def minSubArrayLen(self, s: int, nums: List[int]) -> int:
    ans = math.inf
    summ = 0
    j = 0

    for i, num in enumerate(nums):
      summ += num
      while summ >= s:
        ans = min(ans, i - j + 1)
        summ -= nums[j]
        j += 1

    return ans if ans != math.inf else 0
```


```
new Solution().minSubArrayLen()
```


---
**Score: 5**