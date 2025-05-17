---
title: 761-Special-Binary-String
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/special-binary-string


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
  def makeLargestSpecial(self, S: str) -> str:
    specials = []
    count = 0

    i = 0
    for j, c in enumerate(S):
      count += 1 if c == '1' else -1
      if count == 0:
        specials.append(
            '1' + self.makeLargestSpecial(S[i + 1:j]) + '0')
        i = j + 1

    return ''.join(sorted(specials)[::-1])
```


```
new Solution().makeLargestSpecial()
```


---
**Score: 5**