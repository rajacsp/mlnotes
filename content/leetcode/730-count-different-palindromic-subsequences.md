---
title: 730-Count-Different-Palindromic-Subsequences
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/count-different-palindromic-subsequences


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
  def countPalindromicSubsequences(self, s: str) -> int:
    def count(l: int, r: int) -> int:
      if l > r:
        return 0
      if l == r:
        return 1
      key = l * len(s) + r
      if key in memo:
        return memo[key]

      if s[l] == s[r]:
        lo = l + 1
        hi = r - 1
        while lo <= hi and s[lo] != s[l]:
          lo += 1
        while lo <= hi and s[hi] != s[l]:
          hi -= 1
        if lo > hi:
          ans = count(l + 1, r - 1) * 2 + 2
        elif lo == hi:
          ans = count(l + 1, r - 1) * 2 + 1
        else:
          ans = count(l + 1, r - 1) * 2 - count(lo + 1, hi - 1)
      else:
        ans = count(l, r - 1) + count(l + 1, r) - count(l + 1, r - 1)

      memo[key] = (ans + kMod) % kMod
      return memo[key]

    kMod = 1_000_000_007
    memo = {}

    return count(0, len(s) - 1)
```


```
new Solution().countPalindromicSubsequences()
```


---
**Score: 5**