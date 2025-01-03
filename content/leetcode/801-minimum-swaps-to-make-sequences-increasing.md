---
title: 801-Minimum-Swaps-To-Make-Sequences-Increasing
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing


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
  def minSwap(self, A: List[int], B: List[int]) -> int:
    keepAt = [math.inf] * len(A)
    swapAt = [math.inf] * len(A)
    keepAt[0] = 0
    swapAt[0] = 1

    for i in range(1, len(A)):
      if A[i] > A[i - 1] and B[i] > B[i - 1]:
        keepAt[i] = keepAt[i - 1]
        swapAt[i] = swapAt[i - 1] + 1
      if A[i] > B[i - 1] and B[i] > A[i - 1]:
        keepAt[i] = min(keepAt[i], swapAt[i - 1])
        swapAt[i] = min(swapAt[i], keepAt[i - 1] + 1)

    return min(keepAt[-1], swapAt[-1])
```


```
new Solution().minSwap()
```


---
**Score: 5**