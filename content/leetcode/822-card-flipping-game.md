---
title: 822-Card-Flipping-Game
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/card-flipping-game


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
  def flipgame(self, fronts: List[int], backs: List[int]) -> int:
    same = {f for f, b in zip(fronts, backs) if f == b}
    return min([num for num in fronts + backs
                if num not in same] or [0])
```


```
new Solution().flipgame()
```


---
**Score: 5**