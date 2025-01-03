---
title: 462-Minimum-Moves-To-Equal-Array-Elements-Ii
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii


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
import statistics


class Solution:
  def minMoves2(self, nums: List[int]) -> int:
    median = int(statistics.median(nums))
    return sum(abs(num - median) for num in nums)
```


```
new Solution().minMoves2()
```


---
**Score: 5**