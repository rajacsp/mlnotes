---
title: 488-Zuma-Game
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/zuma-game


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
  def findMinStep(self, board: str, hand: str) -> int:
    def deDup(board):
      start = 0  # Start index of a color sequenece
      for i, c in enumerate(board):
        if c != board[start]:
          if i - start >= 3:
            return deDup(board[:start] + board[i:])
          start = i  # Meet a new sequence
      return board

    @functools.lru_cache(None)
    def dfs(board: str, hand: str):
      board = deDup(board)
      if board == '#':
        return 0

      boardSet = set(board)
      # Hand that in board
      hand = ''.join(h for h in hand if h in boardSet)
      if not hand:  # Infeasible
        return math.inf

      ans = math.inf

      for i in range(len(board)):
        for j, h in enumerate(hand):
          # Place hs[j] in board[i]
          newHand = hand[:j] + hand[j + 1:]
          newBoard = board[:i] + h + board[i:]
          ans = min(ans, 1 + dfs(newBoard, newHand))

      return ans

    ans = dfs(board + '#', hand)
    return -1 if ans == math.inf else ans
```


```
new Solution().findMinStep()
```


---
**Score: 5**