---
title: 1015-Smallest-Integer-Divisible-By-K
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/smallest-integer-divisible-by-k


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
  def smallestRepunitDivByK(self, K: int) -> int:
    if K % 10 not in {1, 3, 7, 9}:
      return -1

    seen = set()
    N = 0

    for length in range(1, K + 1):
      N = (N * 10 + 1) % K
      if N == 0:
        return length
      if N in seen:
        return -1
      seen.add(N)

    return -1
```


```
new Solution().smallestRepunitDivByK()
```


---
**Score: 5**