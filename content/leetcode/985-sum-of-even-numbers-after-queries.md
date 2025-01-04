---
title: 985-Sum-Of-Even-Numbers-After-Queries
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/sum-of-even-numbers-after-queries


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
  def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
    ans = []
    summ = sum(a for a in A if a % 2 == 0)

    for q in queries:
      if A[q[1]] % 2 == 0:
        summ -= A[q[1]]
      A[q[1]] += q[0]
      if A[q[1]] % 2 == 0:
        summ += A[q[1]]
      ans.append(summ)

    return ans
```


```
new Solution().sumEvenAfterQueries()
```


---
**Score: 5**