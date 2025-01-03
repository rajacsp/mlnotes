---
title: 949-Largest-Time-For-Given-Digits
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/largest-time-for-given-digits


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
  def largestTimeFromDigits(self, A: List[int]) -> str:
    for time in itertools.permutations(sorted(A, reverse=True)):
      if time[:2] < (2, 4) and time[2] < 6:
        return '%d%d:%d%d' % time

    return ''
```


```
new Solution().largestTimeFromDigits()
```


---
**Score: 5**