---
title: 753-Cracking-The-Safe
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/cracking-the-safe


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
  def crackSafe(self, n: int, k: int) -> str:
    passwordSize = k**n
    path = '0' * n
    seen = set()
    seen.add(path)

    def dfs(path: str) -> str:
      if len(seen) == passwordSize:
        return path

      for c in map(str, range(k)):
        node = path[-n + 1:] + c if n > 1 else c
        if node not in seen:
          seen.add(node)
          res = dfs(path + c)
          if res:
            return res
          seen.remove(node)

    return dfs(path)
```


```
new Solution().crackSafe()
```


---
**Score: 5**