---
title: 36-Valid-Sudoku
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/valid-sudoku


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
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    seen = set()

    for i in range(9):
      for j in range(9):
        c = board[i][j]
        if c == '.':
          continue
        if c + '@row ' + str(i) in seen or \
           c + '@col ' + str(j) in seen or \
           c + '@box ' + str(i // 3) + str(j // 3) in seen:
          return False
        seen.add(c + '@row ' + str(i))
        seen.add(c + '@col ' + str(j))
        seen.add(c + '@box ' + str(i // 3) + str(j // 3))

    return True
```


```
new Solution().isValidSudoku()
```


---
**Score: 5**