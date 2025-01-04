---
title: 672-Bulb-Switcher-Ii
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/bulb-switcher-ii


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
  def flipLights(self, n: int, m: int) -> int:
    n = min(n, 3)

    if m == 0:
      return 1
    if m == 1:
      return [2, 3, 4][n - 1]
    if m == 2:
      return [2, 4, 7][n - 1]

    return [2, 4, 8][n - 1]
```


```
new Solution().flipLights()
```


---
**Score: 5**