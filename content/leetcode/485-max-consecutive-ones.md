---
title: 485-Max-Consecutive-Ones
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/max-consecutive-ones


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
  def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    ans = 0
    summ = 0

    for num in nums:
      if num == 0:
        summ = 0
      else:
        summ += num
        ans = max(ans, summ)

    return ans
```


```
new Solution().findMaxConsecutiveOnes()
```


---
**Score: 5**