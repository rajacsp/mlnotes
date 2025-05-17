---
title: 458-Poor-Pigs
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/poor-pigs


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
  def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
    return ceil(log(buckets) / log(minutesToTest // minutesToDie + 1))
```


```
new Solution().poorPigs()
```


---
**Score: 5**