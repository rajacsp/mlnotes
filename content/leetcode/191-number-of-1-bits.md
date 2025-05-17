---
title: 191-Number-Of-1-Bits
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/number-of-1-bits


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
  def hammingWeight(self, n: int) -> int:
    ans = 0

    for i in range(32):
      if (n >> i) & 1:
        ans += 1

    return ans
```


```
new Solution().hammingWeight()
```


---
**Score: 5**