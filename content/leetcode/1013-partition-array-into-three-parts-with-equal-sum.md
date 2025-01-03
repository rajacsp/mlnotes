---
title: 1013-Partition-Array-Into-Three-Parts-With-Equal-Sum
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum


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
  def canThreePartsEqualSum(self, A: List[int]) -> bool:
    summ = sum(A)
    prefix = 0
    parts = 1

    for a in A:
      prefix += a
      if prefix == summ * parts // 3:
        parts += 1

    return summ % 3 == 0 and parts >= 3
```


```
new Solution().canThreePartsEqualSum()
```


---
**Score: 5**