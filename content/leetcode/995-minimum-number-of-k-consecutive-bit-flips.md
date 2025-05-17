---
title: 995-Minimum-Number-Of-K-Consecutive-Bit-Flips
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips


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
  def minKBitFlips(self, A: List[int], K: int) -> int:
    ans = 0
    flippedTime = 0

    for r, a in enumerate(A):
      if r >= K and A[r - K] == 2:
        flippedTime -= 1
      if flippedTime % 2 == a:
        if r + K > len(A):
          return -1
        ans += 1
        flippedTime += 1
        A[r] = 2

    return ans
```


```
new Solution().minKBitFlips()
```


---
**Score: 5**