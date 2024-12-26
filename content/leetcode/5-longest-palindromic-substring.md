---
title: 5-Longest-Palindromic-Substring
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/longest-palindromic-substring


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
  def longestPalindrome(self, s: str) -> str:
    if not s:
      return ''

    indices = [0, 0]

    # Returns [start, end] indices of the longest palindrome extended from s[i..j]
    def extend(s: str, i: int, j: int) -> Tuple[int, int]:
      while i >= 0 and j < len(s):
        if s[i] != s[j]:
          break
        i -= 1
        j += 1
      return i + 1, j - 1

    for i in range(len(s)):
      l1, r1 = extend(s, i, i)
      if r1 - l1 > indices[1] - indices[0]:
        indices = l1, r1
      if i + 1 < len(s) and s[i] == s[i + 1]:
        l2, r2 = extend(s, i, i + 1)
        if r2 - l2 > indices[1] - indices[0]:
          indices = l2, r2

    return s[indices[0]:indices[1] + 1]
```


```
new Solution().longestPalindrome()
```


---
**Score: 5**