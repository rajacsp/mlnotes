---
title: 954-Array-Of-Doubled-Pairs
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/array-of-doubled-pairs


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
  def canReorderDoubled(self, A: List[int]) -> bool:
    count = Counter(A)

    for key in sorted(count, key=abs):
      if count[key] > count[2 * key]:
        return False
      count[2 * key] -= count[key]

    return True
```


```
new Solution().canReorderDoubled()
```


---
**Score: 5**