---
title: 293-Flip-Game
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/flip-game


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
  def generatePossibleNextMoves(self, currentState: str) -> List[str]:
    return [currentState[:i] + '--' + currentState[i + 2:]
            for i, (a, b) in enumerate(zip(currentState, currentState[1:]))
            if a == '+' and b == '+']
```


```
new Solution().generatePossibleNextMoves()
```


---
**Score: 5**