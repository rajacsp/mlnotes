---
title: 186-Reverse-Words-In-A-String-Ii
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/reverse-words-in-a-string-ii


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
  def reverseWords(self, s: List[str]) -> None:
    def reverse(l: int, r: int) -> None:
      while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

    def reverseWords(n: int) -> None:
      i = 0
      j = 0

      while i < n:
        while i < j or (i < n and s[i] == ' '):  # Skip spaces
          i += 1
        while j < i or (j < n and s[j] != ' '):  # Skip non spaces
          j += 1
        reverse(i, j - 1)  # Reverse the word

    reverse(0, len(s) - 1)  # Reverse the whole string
    reverseWords(len(s))  # Reverse each word
```


```
new Solution().reverseWords()
```


---
**Score: 5**