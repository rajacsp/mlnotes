---
title: 171-Excel-Sheet-Column-Number
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/excel-sheet-column-number


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
  def titleToNumber(self, s: str) -> int:
    ans = 0

    for c in s:
      ans = ans * 26 + ord(c) - ord('@')

    return ans
```


```
new Solution().titleToNumber()
```


---
**Score: 5**