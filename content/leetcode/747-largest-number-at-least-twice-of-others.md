---
title: 747-Largest-Number-At-Least-Twice-Of-Others
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/largest-number-at-least-twice-of-others


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
  def dominantIndex(self, nums: List[int]) -> int:
    max = 0
    secondMax = 0

    for i, num in enumerate(nums):
      if num > max:
        secondMax = max
        max = num
        ans = i
      elif num > secondMax:
        secondMax = num

    return ans if max >= 2 * secondMax else -1
```


```
new Solution().dominantIndex()
```


---
**Score: 5**