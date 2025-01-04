---
title: 410-Split-Array-Largest-Sum
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/split-array-largest-sum


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
  def splitArray(self, nums: List[int], m: int) -> int:
    n = len(nums)
    prefix = [0] + list(itertools.accumulate(nums))

    # Dp(i, k) := min of largest sum to split first i nums into k groups
    @functools.lru_cache(None)
    def dp(i: int, k: int) -> int:
      if k == 1:
        return prefix[i]

      ans = math.inf

      # Try all possible partitions
      for j in range(k - 1, i):
        ans = min(ans, max(dp(j, k - 1), prefix[i] - prefix[j]))

      return ans

    return dp(n, m)
```


```
new Solution().splitArray()
```


---
**Score: 5**