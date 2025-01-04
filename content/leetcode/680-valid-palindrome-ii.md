---
title: 680-Valid-Palindrome-Ii
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/valid-palindrome-ii


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
  def validPalindrome(self, s: str) -> bool:
    def validPalindrome(l: int, r: int) -> bool:
      return all(s[i] == s[r - i + l] for i in range(l, (l + r) // 2 + 1))

    n = len(s)

    for i in range(n // 2):
      if s[i] != s[~i]:
        return validPalindrome(i + 1, n - 1 - i) or validPalindrome(i, n - 2 - i)

    return True
```


```
new Solution().validPalindrome()
```


---
**Score: 5**