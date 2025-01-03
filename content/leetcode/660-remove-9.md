---
title: 660-Remove-9
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/remove-9


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
  def newInteger(self, n: int) -> int:
    ans = []
    while n:
      ans.append(str(n % 9))
      n //= 9
    return ''.join(reversed(ans))
```


```
new Solution().newInteger()
```


---
**Score: 5**