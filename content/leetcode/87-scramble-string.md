---
title: 87-Scramble-String
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/scramble-string


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
  def isScramble(self, s1: str, s2: str) -> bool:
    if s1 == s2:
      return True
    if len(s1) != len(s2):
      return False
    if Counter(s1) != Counter(s2):
      return False

    for i in range(1, len(s1)):
      if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
        return True
      if self.isScramble(s1[:i], s2[len(s2) - i:]) and self.isScramble(s1[i:], s2[:len(s2) - i]):
        return True

    return False
```


```
new Solution().isScramble()
```


---
**Score: 5**