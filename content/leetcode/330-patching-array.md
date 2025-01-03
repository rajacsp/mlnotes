---
title: 330-Patching-Array
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/patching-array


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
  def minPatches(self, nums: List[int], n: int) -> int:
    ans = 0
    i = 0     # Point to nums
    miss = 1  # Min sum in [1, n] we might miss

    while miss <= n:
      if i < len(nums) and nums[i] <= miss:
        miss += nums[i]
        i += 1
      else:
        # Greedily add miss itself to increase the range
        # From [1, miss) to [1, 2 * miss)
        miss += miss
        ans += 1

    return ans
```


```
new Solution().minPatches()
```


---
**Score: 5**