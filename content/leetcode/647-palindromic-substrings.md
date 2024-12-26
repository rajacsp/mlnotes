---
title: 647-Palindromic-Substrings
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/palindromic-substrings


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
  def countSubstrings(self, s: str) -> int:
    def extendPalindromes(l: int, r: int) -> int:
      count = 0

      while l >= 0 and r < len(s) and s[l] == s[r]:
        count += 1
        l -= 1
        r += 1

      return count

    ans = 0

    for i in range(len(s)):
      ans += extendPalindromes(i, i)
      ans += extendPalindromes(i, i + 1)

    return ans
```


```
new Solution().countSubstrings()
```


---
**Score: 5**