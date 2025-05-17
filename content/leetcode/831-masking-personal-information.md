---
title: 831-Masking-Personal-Information
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/masking-personal-information


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
  def maskPII(self, S: str) -> str:
    atIndex = S.find('@')
    if atIndex != -1:
      S = S.lower()
      return S[0] + '*' * 5 + S[atIndex - 1:]

    ans = ''.join(c for c in S if c.isdigit())

    if len(ans) == 10:
      return '***-***-' + ans[-4:]
    return '+' + '*' * (len(ans) - 10) + '-***-***-' + ans[-4:]
```


```
new Solution().maskPII()
```


---
**Score: 5**