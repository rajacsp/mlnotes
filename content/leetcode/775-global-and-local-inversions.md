---
title: 775-Global-And-Local-Inversions
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/global-and-local-inversions


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
  def isIdealPermutation(self, A: List[int]) -> bool:
    for i, a in enumerate(A):
      if abs(a - i) > 1:
        return False

    return True
```


```
new Solution().isIdealPermutation()
```


---
**Score: 5**