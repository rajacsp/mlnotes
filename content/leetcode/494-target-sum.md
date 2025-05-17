---
title: 494-Target-Sum
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/target-sum


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
  def findTargetSumWays(self, nums: List[int], target: int) -> int:
    summ = sum(nums)
    if summ < abs(target) or (summ + target) & 1:
      return 0

    def knapsack(target: int) -> int:
      # dp[i] := # Of ways to sum to i by nums so far
      dp = [1] + [0] * summ

      for num in nums:
        for j in range(summ, num - 1, -1):
          dp[j] += dp[j - num]

      return dp[target]

    return knapsack((summ + target) // 2)
```


```
new Solution().findTargetSumWays()
```


---
**Score: 5**