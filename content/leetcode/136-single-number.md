---
title: 136-Single-Number
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/single-number


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
  def singleNumber(self, nums: List[int]) -> int:
    return functools.reduce(lambda x, y: x ^ y, nums, 0)
```


```
new Solution().singleNumber()
```


---
**Score: 5**