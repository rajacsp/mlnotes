---
title: 717-1-Bit-And-2-Bit-Characters
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/1-bit-and-2-bit-characters


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
  def isOneBitCharacter(self, bits: List[int]) -> bool:
    i = 0
    while i < len(bits) - 1:
      i += bits[i] + 1

    return i == len(bits) - 1
```


```
new Solution().isOneBitCharacter()
```


---
**Score: 5**