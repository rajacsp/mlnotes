---
title: 96-Unique-Binary-Search-Trees
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/unique-binary-search-trees


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
  def numTrees(self, n: int) -> int:
    # G[i] := # Of unique BST's that store values 1..i
    G = [1, 1] + [0] * (n - 1)

    for i in range(2, n + 1):
      for j in range(i):
        G[i] += G[j] * G[i - j - 1]

    return G[n]
```


```
new Solution().numTrees()
```


---
**Score: 5**