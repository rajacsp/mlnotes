---
title: 945-Minimum-Increment-To-Make-Array-Unique
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/minimum-increment-to-make-array-unique


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
  def minIncrementForUnique(self, A: List[int]) -> int:
    ans = 0
    minAvailable = 0

    A.sort()

    for a in A:
      ans += max(minAvailable - a, 0)
      minAvailable = max(minAvailable, a) + 1

    return ans
```


```
new Solution().minIncrementForUnique()
```


---
**Score: 5**