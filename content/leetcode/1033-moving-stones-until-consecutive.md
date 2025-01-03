---
title: 1033-Moving-Stones-Until-Consecutive
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/moving-stones-until-consecutive


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
  def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
    nums = sorted([a, b, c])

    if nums[2] - nums[0] == 2:
      return [0, 0]
    return [1 if min(nums[1] - nums[0], nums[2] - nums[1]) <= 2 else 2,
            nums[2] - nums[0] - 2]
```


```
new Solution().numMovesStones()
```


---
**Score: 5**