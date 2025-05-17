---
title: 55-Jump-Game
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/jump-game


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
  def canJump(self, nums: List[int]) -> bool:
    i = 0
    reach = 0

    while i < len(nums) and i <= reach:
      reach = max(reach, i + nums[i])
      i += 1

    return i == len(nums)
```


```
new Solution().canJump()
```


---
**Score: 5**