---
title: 794-Valid-Tic-Tac-Toe-State
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/valid-tic-tac-toe-state


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
  def validTicTacToe(self, board: List[str]) -> bool:
    def isWin(c: chr) -> bool:
      return any(row.count(c) == 3 for row in board) or \
          any(row.count(c) == 3 for row in list(zip(*board))) or \
          all(board[i][i] == c for i in range(3)) or \
          all(board[i][2 - i] == c for i in range(3))

    countX = sum(row.count('X') for row in board)
    countO = sum(row.count('O') for row in board)

    if countX < countO or countX - countO > 1:
      return False
    if isWin('X') and countX == countO or isWin('O') and countX != countO:
      return False

    return True
```


```
new Solution().validTicTacToe()
```


---
**Score: 5**