---
title: 926-Flip-String-To-Monotone-Increasing
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/flip-string-to-monotone-increasing


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
  def minFlipsMonoIncr(self, S: str) -> int:
    dp = [0] * 2

    for i, c in enumerate(S):
      dp[0], dp[1] = dp[0] + (c == '1'), min(dp[0], dp[1]) + (c == '0')

    return min(dp[0], dp[1])
```


```
new Solution().minFlipsMonoIncr()
```


---
**Score: 5**