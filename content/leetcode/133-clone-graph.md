---
title: 133-Clone-Graph
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/clone-graph


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
  def cloneGraph(self, node: 'Node') -> 'Node':
    if not node:
      return None

    q = deque([node])
    map = {node: Node(node.val)}

    while q:
      u = q.popleft()
      for v in u.neighbors:
        if v not in map:
          map[v] = Node(v.val)
          q.append(v)
        map[u].neighbors.append(map[v])

    return map[node]
```


```
new Solution().cloneGraph()
```


---
**Score: 5**