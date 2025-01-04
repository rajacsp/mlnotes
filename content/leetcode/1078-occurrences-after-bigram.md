---
title: 1078-Occurrences-After-Bigram
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/occurrences-after-bigram


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
  def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
    words = text.split()
    return [c for a, b, c in zip(words, words[1:], words[2:]) if a == first and b == second]
```


```
new Solution().findOcurrences()
```


---
**Score: 5**