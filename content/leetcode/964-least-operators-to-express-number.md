---
title: 964-Least-Operators-To-Express-Number
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/least-operators-to-express-number


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
  def leastOpsExpressTarget(self, x: int, target: int) -> int:
    @functools.lru_cache(None)
    def dfs(target):
      if x > target:
        return min(2 * target - 1, 2 * (x - target))
      if x == target:
        return 0

      prod = x
      n = 0
      while prod < target:
        prod *= x
        n += 1
      if prod == target:
        return n

      ans = dfs(target - prod // x) + n
      if prod < 2 * target:
        ans = min(ans, dfs(prod - target) + n + 1)
      return ans

    return dfs(target)
```


```
new Solution().leastOpsExpressTarget()
```


---
**Score: 5**