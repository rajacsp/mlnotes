---
title: 453-Minimum-Moves-To-Equal-Array-Elements
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/minimum-moves-to-equal-array-elements


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
  def minMoves(self, nums: List[int]) -> int:
    mini = min(nums)
    return sum(num - mini for num in nums)
```


```
new Solution().minMoves()
```


---
**Score: 5**