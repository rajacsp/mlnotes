---
title: 138-Copy-List-With-Random-Pointer
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/copy-list-with-random-pointer


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
  def copyRandomList(self, head: 'Node') -> 'Node':
    if not head:
      return None
    if head in self.map:
      return self.map[head]

    newNode = Node(head.val)
    self.map[head] = newNode
    newNode.next = self.copyRandomList(head.next)
    newNode.random = self.copyRandomList(head.random)
    return newNode

  map = {}
```


```
new Solution().copyRandomList()
```


---
**Score: 5**