---
title: 888-Fair-Candy-Swap
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/fair-candy-swap


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
  def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
    diff = (sum(A) - sum(B)) // 2
    B = set(B)

    for a in A:
      if a - diff in B:
        return [a, a - diff]
```


```
new Solution().fairCandySwap()
```


---
**Score: 5**