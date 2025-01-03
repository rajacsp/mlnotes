---
title: 849-Maximize-Distance-To-Closest-Person
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/maximize-distance-to-closest-person


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
  def maxDistToClosest(self, seats: List[int]) -> int:
    n = len(seats)
    ans = 0
    j = -1

    for i in range(n):
      if seats[i] == 1:
        ans = i if j == -1 else max(ans, (i - j) // 2)
        j = i

    return max(ans, n - j - 1)
```


```
new Solution().maxDistToClosest()
```


---
**Score: 5**