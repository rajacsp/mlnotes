---
title: 756-Pyramid-Transition-Matrix
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/pyramid-transition-matrix


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
  def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
    prefixToBlocks = defaultdict(list)

    for a in allowed:
      prefixToBlocks[a[:2]].append(a[2])

    def dfs(row: str, nextRow: str, i: int) -> bool:
      if len(row) == 1:
        return True
      if len(nextRow) + 1 == len(row):
        return dfs(nextRow, '', 0)

      for c in prefixToBlocks[row[i:i + 2]]:
        if dfs(row, nextRow + c, i + 1):
          return True

      return False

    return dfs(bottom, '', 0)
```


```
new Solution().pyramidTransition()
```


---
**Score: 5**