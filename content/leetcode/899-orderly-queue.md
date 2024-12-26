---
title: 899-Orderly-Queue
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/orderly-queue


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
  def orderlyQueue(self, S: str, K: int) -> str:
    return ''.join(sorted(S)) if K > 1 else min(S[i:] + S[:i] for i in range(len(S)))
```


```
new Solution().orderlyQueue()
```


---
**Score: 5**