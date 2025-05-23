---
title: 909-Snakes-And-Ladders
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/snakes-and-ladders


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
  def snakesAndLadders(self, board: List[List[int]]) -> int:
    n = len(board)
    ans = 0
    q = deque([1])
    seen = set()
    A = [0] * (1 + n * n)  # 2D -> 1D

    for i in range(n):
      for j in range(n):
        A[(n - 1 - i) * n + (j + 1 if n - i & 1 else n - j)] = board[i][j]

    while q:
      ans += 1
      for _ in range(len(q)):
        curr = q.popleft()
        for next in range(curr + 1, min(curr + 6, n * n) + 1):
          dest = A[next] if A[next] > 0 else next
          if dest == n * n:
            return ans
          if dest in seen:
            continue
          q.append(dest)
          seen.add(dest)

    return -1
```


```
new Solution().snakesAndLadders()
```


---
**Score: 5**