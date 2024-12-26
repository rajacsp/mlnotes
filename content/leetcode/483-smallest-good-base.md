---
title: 483-Smallest-Good-Base
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/smallest-good-base


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
  def smallestGoodBase(self, n: str) -> str:
    n = int(n)

    for m in range(int(math.log(n, 2)), 1, -1):
      k = int(n**m**-1)
      if (k**(m + 1) - 1) // (k - 1) == n:
        return str(k)

    return str(n - 1)
```


```
new Solution().smallestGoodBase()
```


---
**Score: 5**