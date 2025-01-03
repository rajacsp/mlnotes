---
title: 789-Escape-The-Ghosts
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/escape-the-ghosts


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
  def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
    ghostSteps = min(abs(x - target[0]) +
                     abs(y - target[1]) for x, y in ghosts)

    return abs(target[0]) + abs(target[1]) < ghostSteps
```


```
new Solution().escapeGhosts()
```


---
**Score: 5**