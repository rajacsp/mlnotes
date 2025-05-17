---
title: 992-Subarrays-With-K-Different-Integers
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/subarrays-with-k-different-integers


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
  def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
    def subarraysWithAtMostKDistinct(K: int) -> int:
      ans = 0
      count = Counter()

      l = 0
      for r, a in enumerate(A):
        count[a] += 1
        if count[a] == 1:
          K -= 1
        while K < 0:
          count[A[l]] -= 1
          if count[A[l]] == 0:
            K += 1
          l += 1
        ans += r - l + 1  # A[l..r], A[l + 1..r], ..., A[r]

      return ans

    return subarraysWithAtMostKDistinct(K) - subarraysWithAtMostKDistinct(K - 1)
```


```
new Solution().subarraysWithKDistinct()
```


---
**Score: 5**