---
title: 294-Flip-Game-Ii
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/flip-game-ii


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
  @functools.lru_cache(None)
  def canWin(self, currentState: str) -> bool:
    # If any of currentState[i:i + 2] == "++" and your friend can't win after
    # Changing currentState[i:i + 2] to "--" (or "-"), then you can win
    return any(True
               for i, (a, b) in enumerate(zip(currentState, currentState[1:]))
               if a == '+' and b == '+' and
               not self.canWin(currentState[:i] + '-' + currentState[i + 2:]))
```


```
new Solution().canWin()
```


---
**Score: 5**