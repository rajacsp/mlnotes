---
title: 90-Subsets-Ii
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/subsets-ii


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
  def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    ans = []

    def dfs(s: int, path: List[int]) -> None:
      ans.append(path)
      if s == len(nums):
        return

      for i in range(s, len(nums)):
        if i > s and nums[i] == nums[i - 1]:
          continue
        dfs(i + 1, path + [nums[i]])

    nums.sort()
    dfs(0, [])
    return ans
```


```
new Solution().subsetsWithDup()
```


---
**Score: 5**