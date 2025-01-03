---
title: 454-4Sum-Ii
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/4sum-ii


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
  def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    count = Counter(a + b for a in A for b in B)

    return sum(count[-c - d] for c in C for d in D)
```


```
new Solution().fourSumCount()
```


---
**Score: 5**