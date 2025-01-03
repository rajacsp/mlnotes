---
title: 848-Shifting-Letters
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/shifting-letters


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
  def shiftingLetters(self, s: str, shifts: List[int]) -> str:
    ans = []

    for i in reversed(range(len(shifts) - 1)):
      shifts[i] += shifts[i + 1]

    for c, shift in zip(s, shifts):
      ans.append(chr((ord(c) - ord('a') + shift) % 26 + ord('a')))

    return ''.join(ans)
```


```
new Solution().shiftingLetters()
```


---
**Score: 5**