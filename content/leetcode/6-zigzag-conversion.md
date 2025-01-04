---
title: 6-Zigzag-Conversion
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/zigzag-conversion


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
  def convert(self, s: str, numRows: int) -> str:
    rows = [''] * numRows
    k = 0
    direction = (numRows == 1) - 1

    for c in s:
      rows[k] += c
      if k == 0 or k == numRows - 1:
        direction *= -1
      k += direction

    return ''.join(rows)
```


```
new Solution().convert()
```


---
**Score: 5**