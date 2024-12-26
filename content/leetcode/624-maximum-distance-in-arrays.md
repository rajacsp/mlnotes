---
title: 624-Maximum-Distance-In-Arrays
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/maximum-distance-in-arrays


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
  def maxDistance(self, arrays: List[List[int]]) -> int:
    ans = 0
    mini = 10000
    maxi = -10000

    for A in arrays:
      ans = max(ans, A[-1] - mini, maxi - A[0])
      mini = min(mini, A[0])
      maxi = max(maxi, A[-1])

    return ans
```


```
new Solution().maxDistance()
```


---
**Score: 5**