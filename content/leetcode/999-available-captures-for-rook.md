---
title: 999-Available-Captures-For-Rook
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/available-captures-for-rook


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
  def numRookCaptures(self, board: List[List[str]]) -> int:
    ans = 0

    for i in range(8):
      for j in range(8):
        if board[i][j] == 'R':
          i0 = i
          j0 = j

    for d in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
      i = i0 + d[0]
      j = j0 + d[1]
      while 0 <= i < 8 and 0 <= j < 8:
        if board[i][j] == 'p':
          ans += 1
        if board[i][j] != '.':
          break
        i += d[0]
        j += d[1]

    return ans
```


```
new Solution().numRookCaptures()
```


---
**Score: 5**