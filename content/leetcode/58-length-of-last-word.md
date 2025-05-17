---
title: 58-Length-Of-Last-Word
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/length-of-last-word


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
  def lengthOfLastWord(self, s: str) -> int:
    i = len(s) - 1

    while i >= 0 and s[i] == ' ':
      i -= 1
    lastIndex = i
    while i >= 0 and s[i] != ' ':
      i -= 1

    return lastIndex - i
```


```
new Solution().lengthOfLastWord()
```


---
**Score: 5**