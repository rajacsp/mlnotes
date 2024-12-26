---
title: 908-Smallest-Range-I
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/smallest-range-i


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
  def smallestRangeI(self, A: List[int], K: int) -> int:
    return max(0, max(A) - min(A) - 2 * K)
```


```
new Solution().smallestRangeI()
```


---
**Score: 5**