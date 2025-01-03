---
title: 168-Excel-Sheet-Column-Title
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/excel-sheet-column-title


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
  def convertToTitle(self, n: int) -> str:
    return self.convertToTitle((n - 1) // 26) + \
        chr(ord('A') + (n - 1) % 26) if n else ''
```


```
new Solution().convertToTitle()
```


---
**Score: 5**