---
title: 841-Keys-And-Rooms
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/keys-and-rooms


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
  def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
    seen = [False] * len(rooms)

    def dfs(node: int) -> None:
      seen[node] = True
      for child in rooms[node]:
        if not seen[child]:
          dfs(child)

    dfs(0)
    return all(seen)
```


```
new Solution().canVisitAllRooms()
```


---
**Score: 5**