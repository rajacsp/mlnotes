---
title: 650-2-Keys-Keyboard
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/2-keys-keyboard


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
  def minSteps(self, n: int) -> int:
    if n <= 1:
      return 0

    # dp[i] := min steps to get i 'A'
    # Copy 'A', then paste 'A' i - 1 times
    dp = [i for i in range(n + 1)]

    for i in range(2, n + 1):
      for j in range(i // 2, 2, -1):
        if i % j == 0:
          dp[i] = dp[j] + i // j  # Paste dp[j] i / j times
          break

    return dp[n]
```


```
new Solution().minSteps()
```


---
**Score: 5**