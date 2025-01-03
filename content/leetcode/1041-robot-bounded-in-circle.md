---
title: 1041-Robot-Bounded-In-Circle
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/robot-bounded-in-circle


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
  def isRobotBounded(self, instructions: str) -> bool:
    x = 0
    y = 0
    d = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for instruction in instructions:
      if instruction == 'G':
        x += directions[d][0]
        y += directions[d][1]
      elif instruction == 'L':
        d = (d + 3) % 4
      else:
        d = (d + 1) % 4

    return (x, y) == (0, 0) or d > 0
```


```
new Solution().isRobotBounded()
```


---
**Score: 5**