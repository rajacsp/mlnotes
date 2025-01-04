---
title: 917-Reverse-Only-Letters
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/reverse-only-letters


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
  def reverseOnlyLetters(self, S: str) -> str:
    S = list(S)
    i = 0
    j = len(S) - 1

    while i < j:
      while i < j and not S[i].isalpha():
        i += 1
      while i < j and not S[j].isalpha():
        j -= 1
      S[i], S[j] = S[j], S[i]
      i += 1
      j -= 1

    return ''.join(S)
```


```
new Solution().reverseOnlyLetters()
```


---
**Score: 5**