---
title: 377-Combination-Sum-Iv
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/combination-sum-iv


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
  def combinationSum4(self, nums: List[int], target: int) -> int:
    dp = [1] + [-1] * target

    def dfs(target: int) -> int:
      if target < 0:
        return 0
      if dp[target] != -1:
        return dp[target]

      dp[target] = sum(dfs(target - num) for num in nums)
      return dp[target]

    return dfs(target)
```


```
new Solution().combinationSum4()
```


---
**Score: 5**