---
title: 970-Powerful-Integers
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/powerful-integers


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
  def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
    xs = {x**i for i in range(20) if x**i < bound}
    ys = {y**i for i in range(20) if y**i < bound}
    return list({i + j for i in xs for j in ys if i + j <= bound})
```


```
new Solution().powerfulIntegers()
```


---
**Score: 5**