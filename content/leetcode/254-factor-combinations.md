---
title: 254-Factor-Combinations
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/factor-combinations


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
  def getFactors(self, n: int) -> List[List[int]]:
    ans = []

    def dfs(n: int, s: int, path: List[int]) -> None:
      if n <= 1:
        if len(path) > 1:
          ans.append(path.copy())
        return

      for i in range(s, n + 1):
        if n % i == 0:
          path.append(i)
          dfs(n // i, i, path)
          path.pop()

    dfs(n, 2, [])  # The smallest factor is 2
    return ans
```


```
new Solution().getFactors()
```


---
**Score: 5**