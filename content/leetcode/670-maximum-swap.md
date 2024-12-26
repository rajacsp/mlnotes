---
title: 670-Maximum-Swap
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/maximum-swap


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
  def maximumSwap(self, num: int) -> int:
    s = list(str(num))
    dict = {c: i for i, c in enumerate(s)}

    for i, c in enumerate(s):
      for digit in reversed(string.digits):
        if digit <= c:
          break
        if digit in dict and dict[digit] > i:
          s[i], s[dict[digit]] = digit, s[i]
          return int(''.join(s))

    return num
```


```
new Solution().maximumSwap()
```


---
**Score: 5**