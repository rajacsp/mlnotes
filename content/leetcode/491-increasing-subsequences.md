---
title: 491-Increasing-Subsequences
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/increasing-subsequences


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
  def findSubsequences(self, nums: List[int]) -> List[List[int]]:
    ans = []

    def dfs(s: int, path: List[int]) -> None:
      if len(path) > 1:
        ans.append(path)

      used = set()

      for i in range(s, len(nums)):
        if nums[i] in used:
          continue
        if not path or nums[i] >= path[-1]:
          used.add(nums[i])
          dfs(i + 1, path + [nums[i]])

    dfs(0, [])
    return ans
```


```
new Solution().findSubsequences()
```


---
**Score: 5**