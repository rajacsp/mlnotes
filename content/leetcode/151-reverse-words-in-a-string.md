---
title: 151-Reverse-Words-In-A-String
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/reverse-words-in-a-string


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
  def reverseWords(self, s: str) -> str:
    return ' '.join(reversed(s.split()))
```


```
new Solution().reverseWords()
```


---
**Score: 5**