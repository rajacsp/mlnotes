---
title: 141-Linked-List-Cycle
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/linked-list-cycle


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
  def hasCycle(self, head: ListNode) -> bool:
    slow = head
    fast = head

    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        return True

    return False
```


```
new Solution().hasCycle()
```


---
**Score: 5**