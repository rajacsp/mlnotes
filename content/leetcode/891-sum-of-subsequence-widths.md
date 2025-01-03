---
title: 891-Sum-Of-Subsequence-Widths
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/sum-of-subsequence-widths


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
  def sumSubseqWidths(self, nums: List[int]) -> int:
    kMod = 1_000_000_007
    n = len(nums)
    ans = 0
    exp = 1

    nums.sort()

    for i in range(n):
      ans += (nums[i] - nums[n - i - 1]) * exp
      ans %= kMod
      exp = exp * 2 % kMod

    return ans
```


```
new Solution().sumSubseqWidths()
```


---
**Score: 5**