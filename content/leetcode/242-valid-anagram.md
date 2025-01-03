---
title: 242-Valid-Anagram
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/valid-anagram


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
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False

    dict = Counter(s)

    for c in t:
      dict[c] -= 1
      if dict[c] < 0:
        return False

    return True
```


```
new Solution().isAnagram()
```


---
**Score: 5**