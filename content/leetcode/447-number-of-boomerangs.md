---
title: 447-Number-Of-Boomerangs
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/number-of-boomerangs


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
  def numberOfBoomerangs(self, points: List[List[int]]) -> int:
    ans = 0

    for x1, y1 in points:
      count = defaultdict(int)
      for x2, y2 in points:
        ans += 2 * count[(x1 - x2)**2 + (y1 - y2)**2]
        count[(x1 - x2)**2 + (y1 - y2)**2] += 1

    return ans
```


```
new Solution().numberOfBoomerangs()
```


---
**Score: 5**