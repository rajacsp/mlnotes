---
title: 116-Populating-Next-Right-Pointers-In-Each-Node
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/populating-next-right-pointers-in-each-node


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
  def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
    if not root:
      return None

    def connectTwoNodes(p, q) -> None:
      if not p:
        return
      p.next = q
      connectTwoNodes(p.left, p.right)
      connectTwoNodes(q.left, q.right)
      connectTwoNodes(p.right, q.left)

    connectTwoNodes(root.left, root.right)
    return root
```


```
new Solution().connect()
```


---
**Score: 5**