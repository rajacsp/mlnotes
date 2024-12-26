---
title: 246-Strobogrammatic-Number
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/strobogrammatic-number


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
  def isStrobogrammatic(self, num: str) -> bool:
    rotated = ['0', '1', 'x', 'x', 'x',
               'x', '9', 'x', '8', '6']
    l = 0
    r = len(num) - 1

    while l <= r:
      if num[l] != rotated[ord(num[r]) - ord('0')]:
        return False
      l += 1
      r -= 1

    return True
```


```
new Solution().isStrobogrammatic()
```


---
**Score: 5**