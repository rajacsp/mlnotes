---
title: 338-Counting-Bits
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/counting-bits


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
  def countBits(self, n: int) -> List[int]:
    # Let f(i) := i's # Of 1's in bitmask
    # F(i) = f(i / 2) + i % 2
    ans = [0] * (n + 1)

    for i in range(1, n + 1):
      ans[i] = ans[i // 2] + (i & 1)

    return ans
```


```
new Solution().countBits()
```


---
**Score: 5**