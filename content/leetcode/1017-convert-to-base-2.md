---
title: 1017-Convert-To-Base-2
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/convert-to-base-2


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
  def baseNeg2(self, N: int) -> str:
    ans = ''

    while N:
      ans = str(N & 1) + ans
      N = -(N >> 1)

    return '0' if ans == '' else ans
```


```
new Solution().baseNeg2()
```


---
**Score: 5**