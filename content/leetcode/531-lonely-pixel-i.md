---
title: 531-Lonely-Pixel-I
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/lonely-pixel-i


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
  def findLonelyPixel(self, picture: List[List[str]]) -> int:
    m = len(picture)
    n = len(picture[0])
    ans = 0
    rows = [0] * m  # rows[i] := # Of Bs in rows i
    cols = [0] * n  # cols[i] := # Of Bs in cols i

    for i in range(m):
      for j in range(n):
        if picture[i][j] == 'B':
          rows[i] += 1
          cols[j] += 1

    for i in range(m):
      if rows[i] == 1:  # Only have to examine the rows when rows[i] == 1
        for j in range(n):
          # After we met the 'B' in this rows, we break and search the next row
          if picture[i][j] == 'B':
            if cols[j] == 1:
              ans += 1
            break

    return ans
```


```
new Solution().findLonelyPixel()
```


---
**Score: 5**