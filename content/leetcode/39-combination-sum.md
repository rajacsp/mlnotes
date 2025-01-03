---
title: 39-Combination-Sum
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/combination-sum


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
  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    ans = []

    def dfs(s: int, target: int, path: List[int]) -> None:
      if target < 0:
        return
      if target == 0:
        ans.append(path.clone())
        return

      for i in range(s, len(candidates)):
        path.append(candidates[i])
        dfs(i, target - candidates[i], path)
        path.pop()

    candidates.sort()
    dfs(0, target, [])
    return ans
```


```
new Solution().combinationSum()
```


---
**Score: 5**