---
title: 874-Walking-Robot-Simulation
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/walking-robot-simulation


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
  def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
    dirs = [0, 1, 0, -1, 0]
    ans = 0
    d = 0  # 0 := north, 1 := east, 2 := south, 3 := west
    x = 0  # Start x
    y = 0  # Start y
    obstaclesSet = {(x, y) for x, y in obstacles}

    for c in commands:
      if c == -1:
        d = (d + 1) % 4
      elif c == -2:
        d = (d + 3) % 4
      else:
        for _ in range(c):
          if (x + dirs[d], y + dirs[d + 1]) in obstaclesSet:
            break
          x += dirs[d]
          y += dirs[d + 1]

      ans = max(ans, x * x + y * y)

    return ans
```


```
new Solution().robotSim()
```


---
**Score: 5**