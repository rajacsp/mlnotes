---
title: 961-N-Repeated-Element-In-Size-2N-Array
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/n-repeated-element-in-size-2n-array


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
  def repeatedNTimes(self, A: List[int]) -> int:
    for i in range(len(A) - 2):
      if A[i] == A[i + 1] or A[i] == A[i + 2]:
        return A[i]

    return A[-1]
```


```
new Solution().repeatedNTimes()
```


---
**Score: 5**