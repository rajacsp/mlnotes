---
title: 583-Delete-Operation-For-Two-Strings
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/delete-operation-for-two-strings


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
  def minDistance(self, word1: str, word2: str) -> int:
    m = len(word1)
    n = len(word2)
    dp = [0] * (n + 1)

    for j in range(n + 1):
      dp[j] = j

    for i in range(1, m + 1):
      newDp = [i] + [0] * n
      for j in range(1, n + 1):
        if word1[i - 1] == word2[j - 1]:
          newDp[j] = dp[j - 1]
        else:
          newDp[j] = min(newDp[j - 1], dp[j]) + 1
      dp = newDp

    return dp[n]
```


```
new Solution().minDistance()
```


---
**Score: 5**