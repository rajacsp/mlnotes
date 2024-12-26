---
title: 125-Valid-Palindrome
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/valid-palindrome


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
  def isPalindrome(self, s: str) -> bool:
    l = 0
    r = len(s) - 1

    while l < r:
      while l < r and not s[l].isalnum():
        l += 1
      while l < r and not s[r].isalnum():
        r -= 1
      if s[l].lower() != s[r].lower():
        return False
      l += 1
      r -= 1

    return True
```


```
new Solution().isPalindrome()
```


---
**Score: 5**