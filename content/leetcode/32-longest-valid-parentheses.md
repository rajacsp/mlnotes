---
title: 32-Longest-Valid-Parentheses
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/longest-valid-parentheses


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
  def longestValidParentheses(self, s: str) -> int:
    s2 = ')' + s
    # dp[i] := Length of longest valid parentheses substring of s2[1..i]
    dp = [0] * len(s2)

    for i in range(1, len(s2)):
      if s2[i] == ')' and s2[i - dp[i - 1] - 1] == '(':
        dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2

    return max(dp)
```


```
new Solution().longestValidParentheses()
```


---
**Score: 5**