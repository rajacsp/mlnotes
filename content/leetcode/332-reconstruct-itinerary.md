---
title: 332-Reconstruct-Itinerary
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/reconstruct-itinerary


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
  def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    ans = []
    graph = defaultdict(list)

    for a, b in reversed(sorted(tickets)):
      graph[a].append(b)

    def dfs(u: str) -> None:
      while u in graph and graph[u]:
        dfs(graph[u].pop())
      ans.append(u)

    dfs('JFK')
    return ans[::-1]
```


```
new Solution().findItinerary()
```


---
**Score: 5**