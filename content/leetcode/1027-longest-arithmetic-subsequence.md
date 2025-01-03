---
title: 1027-Longest-Arithmetic-Subsequence
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/longest-arithmetic-subsequence


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
  def longestArithSeqLength(self, nums: List[int]) -> int:
    n = len(nums)
    ans = 0
    # dp[i][k] := length of the longest arithmetic subseq ofnums
    # nums[0..i] with k = diff + 500
    dp = [[0] * 1001 for _ in range(n)]

    for i in range(n):
      for j in range(i):
        k = nums[i] - nums[j] + 500
        dp[i][k] = max(2, dp[j][k] + 1)
        ans = max(ans, dp[i][k])

    return ans
```


```
new Solution().longestArithSeqLength()
```


---
**Score: 5**