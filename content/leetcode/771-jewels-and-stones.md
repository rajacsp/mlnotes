---
title: 771-Jewels-And-Stones
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/jewels-and-stones


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
  def numJewelsInStones(self, J: str, S: str) -> int:
    jewels = set(J)
    return sum(s in jewels for s in S)
```


```
new Solution().numJewelsInStones()
```


---
**Score: 5**