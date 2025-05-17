---
title: 438-Find-All-Anagrams-In-A-String
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/find-all-anagrams-in-a-string


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
  def findAnagrams(self, s: str, p: str) -> List[int]:
    ans = []
    count = Counter(p)
    required = len(p)

    for r, c in enumerate(s):
      count[c] -= 1
      if count[c] >= 0:
        required -= 1
      if r >= len(p):
        count[s[r - len(p)]] += 1
        if count[s[r - len(p)]] > 0:
          required += 1
      if required == 0:
        ans.append(r - len(p) + 1)

    return ans
```


```
new Solution().findAnagrams()
```


---
**Score: 5**