---
title: 541-Reverse-String-Ii
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/reverse-string-ii


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
  def reverseStr(self, s: str, k: int) -> str:
    return s[:k][::-1] + s[k:2 * k] + self.reverseStr(s[2 * k:], k) if s else ""
```


```
new Solution().reverseStr()
```


---
**Score: 5**