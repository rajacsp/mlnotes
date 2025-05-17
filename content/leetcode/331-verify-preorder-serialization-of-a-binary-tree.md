---
title: 331-Verify-Preorder-Serialization-Of-A-Binary-Tree
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree


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
  def isValidSerialization(self, preorder: str) -> bool:
    degree = 1  # OutDegree (children) - inDegree (parent)

    for node in preorder.split(','):
      degree -= 1
      if degree < 0:
        return False
      if node != '#':
        degree += 2

    return degree == 0
```


```
new Solution().isValidSerialization()
```


---
**Score: 5**