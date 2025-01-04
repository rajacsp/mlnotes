---
title: 430-Flatten-A-Multilevel-Doubly-Linked-List
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list


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
  def flatten(self, head: 'Node') -> 'Node':
    def flatten(head: 'Node', rest: 'Node') -> 'Node':
      if not head:
        return rest

      head.next = flatten(head.child, flatten(head.next, rest))
      if head.next:
        head.next.prev = head
      head.child = None
      return head

    return flatten(head, None)
```


```
new Solution().flatten()
```


---
**Score: 5**