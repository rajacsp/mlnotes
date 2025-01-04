---
title: 354-Russian-Doll-Envelopes
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/russian-doll-envelopes


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
  def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    # Same as 300. Longest Increasing Subsequence
    ans = 0
    dp = [0] * len(envelopes)

    for _, h in envelopes:
      l = 0
      r = ans
      while l < r:
        m = (l + r) // 2
        if dp[m] >= h:
          r = m
        else:
          l = m + 1
      dp[l] = h
      if l == ans:
        ans += 1

    return ans
```


```
new Solution().maxEnvelopes()
```


---
**Score: 5**