---
title: 795-Number-Of-Subarrays-With-Bounded-Maximum
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum


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
  def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
    ans = 0
    l = -1
    r = -1

    for i, a in enumerate(A):
      if a > R:
        l = i
      if a >= L:
        r = i
      ans += r - l

    return ans
```


```
new Solution().numSubarrayBoundedMax()
```


---
**Score: 5**