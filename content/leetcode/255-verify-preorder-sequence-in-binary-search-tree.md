---
title: 255-Verify-Preorder-Sequence-In-Binary-Search-Tree
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree


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
  def verifyPreorder(self, preorder: List[int]) -> bool:
    i = 0

    def dfs(min: int, max: int) -> None:
      nonlocal i
      if i == len(preorder):
        return
      if preorder[i] < min or preorder[i] > max:
        return

      val = preorder[i]
      i += 1
      dfs(min, val)
      dfs(val, max)

    dfs(-math.inf, math.inf)
    return i == len(preorder)
```


```
new Solution().verifyPreorder()
```


---
**Score: 5**