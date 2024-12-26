---
title: 533-Lonely-Pixel-Ii
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/lonely-pixel-ii


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
  def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
    m = len(picture)
    n = len(picture[0])
    ans = 0
    rows = [row.count('B') for row in picture]
    cols = [col.count('B') for col in zip(*picture)]
    rowStrings = [''.join(row) for row in picture]
    countRowStrings = Counter(rowStrings)

    for i, (row, stringRow) in enumerate(zip(rows, rowStrings)):
      if row == target and countRowStrings[stringRow] == target:
        for j, col in enumerate(cols):
          if picture[i][j] == 'B' and col == target:
            ans += 1

    return ans
```


```
new Solution().findBlackPixel()
```


---
**Score: 5**