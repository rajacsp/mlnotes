---
title: 375-Guess-Number-Higher-Or-Lower-Ii
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/guess-number-higher-or-lower-ii


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
  def getMoneyAmount(self, n: int) -> int:
    # Dp(i, j) := min money you need to guarantee a win of picking i..j
    @functools.lru_cache(None)
    def dp(i: int, j: int) -> int:
      if i >= j:
        return 0

      ans = math.inf

      for k in range(i, j + 1):
        ans = min(ans, max(dp(i, k - 1), dp(k + 1, j)) + k)

      return ans

    return dp(1, n)
```


```
new Solution().getMoneyAmount()
```


---
**Score: 5**