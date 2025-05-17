---
title: 925-Long-Pressed-Name
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/long-pressed-name


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
  def isLongPressedName(self, name: str, typed: str) -> bool:
    i = 0

    for j, t in enumerate(typed):
      if i < len(name) and name[i] == t:
        i += 1
      elif j == 0 or t != typed[j - 1]:
        return False

    return i == len(name)
```


```
new Solution().isLongPressedName()
```


---
**Score: 5**