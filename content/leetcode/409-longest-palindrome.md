---
title: 409-Longest-Palindrome
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/longest-palindrome


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
  def longestPalindrome(self, s: str) -> int:
    ans = 0
    count = Counter(s)

    for c in count.values():
      ans += c if c % 2 == 0 else c - 1

    hasOddCount = any(c % 2 == 1 for c in count.values())

    return ans + hasOddCount
```


```
new Solution().longestPalindrome()
```


---
**Score: 5**