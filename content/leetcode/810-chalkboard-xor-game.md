---
title: 810-Chalkboard-Xor-Game
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/chalkboard-xor-game


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
  def xorGame(self, nums: List[int]) -> bool:
    return functools.reduce(operator.xor, nums) == 0 or len(nums) % 2 == 0
```


```
new Solution().xorGame()
```


---
**Score: 5**