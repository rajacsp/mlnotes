---
title: 214-Shortest-Palindrome
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/shortest-palindrome


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
  def shortestPalindrome(self, s: str) -> str:
    t = s[::-1]

    for i in range(len(t)):
      if s.startswith(t[i:]):
        return t[:i] + s

    return t + s
```


```
new Solution().shortestPalindrome()
```


---
**Score: 5**