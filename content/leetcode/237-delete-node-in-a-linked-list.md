---
title: 237-Delete-Node-In-A-Linked-List
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/delete-node-in-a-linked-list


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
  def deleteNode(self, node):
    node.val = node.next.val
    node.next = node.next.next
```


```
new Solution().deleteNode()
```


---
**Score: 5**