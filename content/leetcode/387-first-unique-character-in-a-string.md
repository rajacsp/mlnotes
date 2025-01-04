---
title: 387-First-Unique-Character-In-A-String
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/first-unique-character-in-a-string


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
  def firstUniqChar(self, s: str) -> int:
    count = Counter(s)

    for i, c in enumerate(s):
      if count[c] == 1:
        return i

    return -1
```


```
new Solution().firstUniqChar()
```


---
**Score: 5**