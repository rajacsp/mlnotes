---
title: 828-Count-Unique-Characters-Of-All-Substrings-Of-A-Given-String
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string


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
  def uniqueLetterString(self, s: str) -> int:
    ans = 0
    count = 0
    lastCount = [0] * 26
    lastSeen = [-1] * 26

    for i, c in enumerate(s):
      c = ord(c) - ord('A')
      currentCount = i - lastSeen[c]
      count = count - lastCount[c] + currentCount
      lastCount[c] = currentCount
      lastSeen[c] = i
      ans += count

    return ans
```


```
new Solution().uniqueLetterString()
```


---
**Score: 5**