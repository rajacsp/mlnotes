---
title: 873-Length-Of-Longest-Fibonacci-Subsequence
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/length-of-longest-fibonacci-subsequence


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
  def lenLongestFibSubseq(self, A: List[int]) -> int:
    n = len(A)
    ans = 0
    numToIndex = {a: i for i, a in enumerate(A)}
    dp = [[2] * n for _ in range(n)]

    for j in range(n):
      for k in range(j + 1, n):
        ai = A[k] - A[j]
        if ai < A[j] and ai in numToIndex:
          i = numToIndex[ai]
          dp[j][k] = dp[i][j] + 1
          ans = max(ans, dp[j][k])

    return ans
```


```
new Solution().lenLongestFibSubseq()
```


---
**Score: 5**