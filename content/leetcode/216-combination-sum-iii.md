---
title: 216-Combination-Sum-Iii
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/combination-sum-iii


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
  def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    ans = []

    def dfs(k: int, n: int, s: int, path: List[int]) -> None:
      if k == 0 and n == 0:
        ans.append(path)
        return
      if k == 0 or n < 0:
        return

      for i in range(s, 10):
        dfs(k - 1, n - i, i + 1, path + [i])

    dfs(k, n, 1, [])
    return ans
```


```
new Solution().combinationSum3()
```


---
**Score: 5**