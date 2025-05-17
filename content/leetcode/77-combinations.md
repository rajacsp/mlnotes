---
title: 77-Combinations
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/combinations


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
  def combine(self, n: int, k: int) -> List[List[int]]:
    ans = []

    def dfs(s: int, path: List[int]) -> None:
      if len(path) == k:
        ans.append(path.copy())
        return

      for i in range(s, n + 1):
        path.append(i)
        dfs(i + 1, path)
        path.pop()

    dfs(1, [])
    return ans
```


```
new Solution().combine()
```


---
**Score: 5**