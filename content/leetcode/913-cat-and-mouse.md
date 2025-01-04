---
title: 913-Cat-And-Mouse
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/cat-and-mouse


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
from enum import IntEnum


class State(IntEnum):
  kDraw = 0
  kMouseWin = 1
  kCatWin = 2


class Solution:
  def catMouseGame(self, graph: List[List[int]]) -> int:
    n = len(graph)
    # Result of (cat, mouse, move)
    # Move := 0 (mouse) // 1 (cat)
    states = [[[0] * 2 for i in range(n)] for j in range(n)]
    outDegree = [[[0] * 2 for i in range(n)] for j in range(n)]
    q = deque()  # (cat, mouse, move, state)

    for cat in range(n):
      for mouse in range(n):
        outDegree[cat][mouse][0] = len(graph[mouse])
        outDegree[cat][mouse][1] = len(graph[cat]) - graph[cat].count(0)

    # Start from states that winner can be determined
    for cat in range(1, n):
      for move in range(2):
        # Mouse is in the hole . kMouseWin
        states[cat][0][move] = int(State.kMouseWin)
        q.append((cat, 0, move, int(State.kMouseWin)))
        # Cat catches mouse . kCatWin
        states[cat][cat][move] = int(State.kCatWin)
        q.append((cat, cat, move, int(State.kCatWin)))

    while q:
      cat, mouse, move, state = q.popleft()
      if cat == 2 and mouse == 1 and move == 0:
        return state
      prevMove = move ^ 1
      for prev in graph[cat if prevMove else mouse]:
        prevCat = prev if prevMove else cat
        if prevCat == 0:  # Invalid
          continue
        prevMouse = mouse if prevMove else prev
        # The state is already determined
        if states[prevCat][prevMouse][prevMove]:
          continue
        if prevMove == 0 and state == int(State.kMouseWin) or \
                prevMove == 1 and state == int(State.kCatWin):
          states[prevCat][prevMouse][prevMove] = state
          q.append((prevCat, prevMouse, prevMove, state))
        else:
          outDegree[prevCat][prevMouse][prevMove] -= 1
          if outDegree[prevCat][prevMouse][prevMove] == 0:
            states[prevCat][prevMouse][prevMove] = state
            q.append((prevCat, prevMouse, prevMove, state))

    return states[2][1][0]
```


```
new Solution().catMouseGame()
```


---
**Score: 5**