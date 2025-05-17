---
title: 805-Split-Array-With-Same-Average
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/split-array-with-same-average


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
  def splitArraySameAverage(self, A: List[int]) -> bool:
    n = len(A)
    summ = sum(A)
    if not any(i * summ % n == 0 for i in range(1, n // 2 + 1)):
      return False

    sums = [set() for _ in range(n // 2 + 1)]
    sums[0].add(0)

    for a in A:
      for i in range(n // 2, 0, -1):
        for val in sums[i - 1]:
          sums[i].add(a + val)

    for i in range(1, n // 2 + 1):
      if i * summ % n == 0 and i * summ // n in sums[i]:
        return True

    return False
```


```
new Solution().splitArraySameAverage()
```


---
**Score: 5**