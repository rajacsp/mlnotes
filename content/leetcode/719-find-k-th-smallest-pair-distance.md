---
title: 719-Find-K-Th-Smallest-Pair-Distance
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/find-k-th-smallest-pair-distance


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
  def smallestDistancePair(self, nums: List[int], k: int) -> int:
    nums.sort()

    l = 0
    r = nums[-1] - nums[0]

    while l < r:
      m = (l + r) // 2
      count = 0

      j = 0
      for i in range(len(nums)):
        while j < len(nums) and nums[j] <= nums[i] + m:
          j += 1
        count += j - i - 1

      if count < k:
        l = m + 1
      else:
        r = m

    return l
```


```
new Solution().smallestDistancePair()
```


---
**Score: 5**