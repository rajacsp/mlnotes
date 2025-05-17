---
title: 868-Binary-Gap
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/binary-gap


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
  def binaryGap(self, n: int) -> int:
    ans = 0
    d = -32  # Distance between any two 1's, initialized to a reasonable small value

    while n:
      if n & 1:
        ans = max(ans, d)
        d = 0
      n //= 2
      d += 1

    return ans
```


```
new Solution().binaryGap()
```


---
**Score: 5**