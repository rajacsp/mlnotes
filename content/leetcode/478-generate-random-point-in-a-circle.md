---
title: 478-Generate-Random-Point-In-A-Circle
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/generate-random-point-in-a-circle


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
  def __init__(self, radius: float, x_center: float, y_center: float):
    self.radius = radius
    self.x_center = x_center
    self.y_center = y_center

  def randPoint(self) -> List[float]:
    length = sqrt(random.uniform(0, 1)) * self.radius
    degree = random.uniform(0, 1) * 2 * math.pi
    x = self.x_center + length * math.cos(degree)
    y = self.y_center + length * math.sin(degree)
    return [x, y]
```


```
new Solution().__init__()
```


---
**Score: 5**