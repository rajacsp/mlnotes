---
title: 91-Decode-Ways
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/decode-ways


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
  def numDecodings(self, s: str) -> int:
    n = len(s)
    # dp[i] := # Of ways to decode s[i..n)
    dp = [0] * n + [1]

    def isValid(a: chr, b=None) -> bool:
      if b:
        return a == '1' or a == '2' and b < '7'
      return a != '0'

    if isValid(s[-1]):
      dp[n - 1] = 1

    for i in reversed(range(n - 1)):
      if isValid(s[i]):
        dp[i] += dp[i + 1]
      if isValid(s[i], s[i + 1]):
        dp[i] += dp[i + 2]

    return dp[0]
```


```
new Solution().numDecodings()
```


---
**Score: 5**