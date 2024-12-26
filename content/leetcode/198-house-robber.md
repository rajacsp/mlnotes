---
title: 198-House-Robber
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/house-robber


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
  def rob(self, nums: List[int]) -> int:
    if not nums:
      return 0
    if len(nums) == 1:
      return nums[0]

    # dp[i]: = max money of robbing nums[0..i]
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
      dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    return dp[-1]
```


```
new Solution().rob()
```


---
**Score: 5**