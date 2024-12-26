---
title: 718-Maximum-Length-Of-Repeated-Subarray
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/maximum-length-of-repeated-subarray


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
  def findLength(self, nums1: List[int], nums2: List[int]) -> int:
    m = len(nums1)
    n = len(nums2)
    ans = 0
    # dp[i][j] := max length of nums1[i:] and nums2[j:]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in reversed(range(m)):
      for j in reversed(range(n)):
        if nums1[i] == nums2[j]:
          dp[i][j] = dp[i + 1][j + 1] + 1
          ans = max(ans, dp[i][j])

    return ans
```


```
new Solution().findLength()
```


---
**Score: 5**