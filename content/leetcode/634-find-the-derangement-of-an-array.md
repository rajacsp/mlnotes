---
title: 634-Find-The-Derangement-Of-An-Array
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/find-the-derangement-of-an-array


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
  def findDerangement(self, n: int) -> int:
    kMod = 1_000_000_007

    @functools.lru_cache(None)
    def dp(i: int) -> int:
      if i == 0:
        return 1
      if i == 1:
        return 0
      return (i - 1) * (dp(i - 1) + dp(i - 2)) % kMod

    return dp(n)
```


```
new Solution().findDerangement()
```


---
**Score: 5**