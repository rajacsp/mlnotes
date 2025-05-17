---
title: 528-Random-Pick-With-Weight
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/random-pick-with-weight


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
  def __init__(self, w: List[int]):
    self.prefix = list(itertools.accumulate(w))

  def pickIndex(self) -> int:
    target = randint(0, self.prefix[-1] - 1)
    l = 0
    r = len(self.prefix)

    while l < r:
      m = (l + r) // 2
      if self.prefix[m] > target:
        r = m
      else:
        l = m + 1

    return l
```


```
new Solution().__init__()
```


---
**Score: 5**