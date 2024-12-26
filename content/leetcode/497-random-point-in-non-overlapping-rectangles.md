---
title: 497-Random-Point-In-Non-Overlapping-Rectangles
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/random-point-in-non-overlapping-rectangles


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
  def __init__(self, rects: List[List[int]]):
    self.rects = rects
    self.areas = list(itertools.accumulate(
        [(x2 - x1 + 1) * (y2 - y1 + 1) for x1, y1, x2, y2 in rects]))

  def pick(self) -> List[int]:
    index = bisect_right(self.areas, randint(0, self.areas[-1] - 1))
    x1, y1, x2, y2 = self.rects[index]
    return [randint(x1, x2), randint(y1, y2)]
```


```
new Solution().__init__()
```


---
**Score: 5**