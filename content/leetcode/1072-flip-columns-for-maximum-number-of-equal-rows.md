---
title: 1072-Flip-Columns-For-Maximum-Number-Of-Equal-Rows
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows


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
  def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
    patterns = [tuple(a ^ row[0] for a in row) for row in matrix]
    return max(Counter(patterns).values())
```


```
new Solution().maxEqualRowsAfterFlips()
```


---
**Score: 5**