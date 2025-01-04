---
title: 1014-Best-Sightseeing-Pair
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/best-sightseeing-pair


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
  def maxScoreSightseeingPair(self, A: List[int]) -> int:
    ans = 0
    bestPrev = 0

    for a in A:
      ans = max(ans, a + bestPrev)
      bestPrev = max(bestPrev, a) - 1

    return ans
```


```
new Solution().maxScoreSightseeingPair()
```


---
**Score: 5**