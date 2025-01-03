---
title: 1016-Binary-String-With-Substrings-Representing-1-To-N
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n


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
  def queryString(self, S: str, N: int) -> bool:
    if N > 1511:
      return False

    for i in range(N, N // 2, -1):
      if format(i, 'b') not in S:
        return False

    return True
```


```
new Solution().queryString()
```


---
**Score: 5**