---
title: 335-Self-Crossing
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/self-crossing


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
  def isSelfCrossing(self, x: List[int]) -> bool:
    if len(x) <= 3:
      return False

    for i in range(3, len(x)):
      if x[i - 2] <= x[i] and x[i - 1] <= x[i - 3]:
        return True
      if i >= 4 and x[i - 1] == x[i - 3] and x[i - 2] <= x[i] + x[i - 4]:
        return True
      if i >= 5 and x[i - 4] <= x[i - 2] and x[i - 2] <= x[i] + x[i - 4] and x[i - 1] <= x[i - 3] and x[i - 3] <= x[i - 1] + x[i - 5]:
        return True

    return False
```


```
new Solution().isSelfCrossing()
```


---
**Score: 5**