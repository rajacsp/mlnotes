---
title: 389-Find-The-Difference
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/find-the-difference


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
  def findTheDifference(self, s: str, t: str) -> str:
    count = Counter(s)

    for i, c in enumerate(t):
      count[c] -= 1
      if count[c] == -1:
        return c
```


```
new Solution().findTheDifference()
```


---
**Score: 5**