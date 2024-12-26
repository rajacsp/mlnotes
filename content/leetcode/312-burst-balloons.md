---
title: 312-Burst-Balloons
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/burst-balloons


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
  def maxCoins(self, nums: List[int]) -> int:
    A = [1] + nums + [1]

    @functools.lru_cache(None)
    def dp(i: int, j: int) -> int:
      if i > j:
        return 0

      return max(dp(i, k - 1) + dp(k + 1, j) + A[i - 1] * A[k] * A[j + 1]
                 for k in range(i, j + 1))

    return dp(1, len(nums))
```


```
new Solution().maxCoins()
```


---
**Score: 5**