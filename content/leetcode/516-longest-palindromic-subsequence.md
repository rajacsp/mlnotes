---
title: 516-Longest-Palindromic-Subsequence
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/longest-palindromic-subsequence


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
  def longestPalindromeSubseq(self, s: str) -> int:
    # Dp(i, j) := LPS's length in s[i..j]
    @functools.lru_cache(None)
    def dp(i: int, j: int) -> int:
      if i > j:
        return 0
      if i == j:
        return 1
      if s[i] == s[j]:
        return 2 + dp(i + 1, j - 1)
      return max(dp(i + 1, j), dp(i, j - 1))

    return dp(0, len(s) - 1)
```


```
new Solution().longestPalindromeSubseq()
```


---
**Score: 5**