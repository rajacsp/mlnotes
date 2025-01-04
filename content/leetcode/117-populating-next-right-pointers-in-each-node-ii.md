---
title: 117-Populating-Next-Right-Pointers-In-Each-Node-Ii
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii


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
  def connect(self, root: 'Node') -> 'Node':
    node = root  # The node just above current needling

    while node:
      dummy = Node(0)  # Dummy node before needling
      # Needle children of node
      needle = dummy
      while node:
        if node.left:  # Needle left child
          needle.next = node.left
          needle = needle.next
        if node.right:  # Needle right child
          needle.next = node.right
          needle = needle.next
        node = node.next
      node = dummy.next  # Move node to the next level

    return root
```


```
new Solution().connect()
```


---
**Score: 5**