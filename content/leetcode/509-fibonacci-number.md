---
title: 509-Fibonacci-Number
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/fibonacci-number


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
  def fib(self, N: int) -> int:
    if N < 2:
      return N

    dp = [0, 0, 1]

    for i in range(2, N + 1):
      dp[0] = dp[1]
      dp[1] = dp[2]
      dp[2] = dp[0] + dp[1]

    return dp[2]
```


```
new Solution().fib()
```


---
**Score: 5**