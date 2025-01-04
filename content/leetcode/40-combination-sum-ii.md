---
title: 40-Combination-Sum-Ii
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/combination-sum-ii


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
  def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    ans = []

    def dfs(s: int, target: int, path: List[int]) -> None:
      if target < 0:
        return
      if target == 0:
        ans.append(path.copy())
        return

      for i in range(s, len(candidates)):
        if i > s and candidates[i] == candidates[i - 1]:
          continue
        path.append(candidates[i])
        dfs(i + 1, target - candidates[i], path)
        path.pop()

    candidates.sort()
    dfs(0, target, [])
    return ans
```


```
new Solution().combinationSum2()
```


---
**Score: 5**