---
title: 869-Reordered-Power-Of-2
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/reordered-power-of-2


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
  def reorderedPowerOf2(self, N: int) -> bool:
    count = Counter(str(N))
    return any(Counter(str(1 << i)) == count for i in range(30))
```


```
new Solution().reorderedPowerOf2()
```


---
**Score: 5**