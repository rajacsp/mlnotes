---
title: 633-Sum-Of-Square-Numbers
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/sum-of-square-numbers


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
  def judgeSquareSum(self, c: int) -> bool:
    l = 0
    r = int(sqrt(c))

    while l <= r:
      summ = l * l + r * r
      if summ == c:
        return True
      if summ < c:
        l += 1
      else:
        r -= 1

    return False
```


```
new Solution().judgeSquareSum()
```


---
**Score: 5**